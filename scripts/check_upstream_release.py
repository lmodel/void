#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Check VoID's Note and vocabulary file against the edition the schema renders.

The schema renders the Vocabulary of Interlinked Datasets (VoID) as two
sources give it: the W3C Interest Group Note of 3 March 2011, which explains
the vocabulary, and the vocabulary file, which declares its classes and
properties. The namespace document at http://rdfs.org/ns/void redirects to a
host that no longer answers, so the file is read from the copy its editors
keep in their repository on GitHub, at the commit pinned below. Neither is
copied here: tests/upstream/void-terms.tsv lists the terms the file declares,
and scripts/extract_void_terms.py writes it from the pinned file.

Four things can change without any change in this repository:

- W3C publishes another edition of the Note, so the latest version of
  https://www.w3.org/TR/void/ is no longer the pinned one;
- the editors change, drop or add a file in the folder of the vocabulary
  file;
- the Note's page links another licence than the pinned one;
- the editors' repository states a licence, where it states none today.

The script reads the Note's latest-version page, and asks the GitHub API for
the editors' repository's licence, the commit its default branch is at, and
the file tree at that commit and at the pinned one. It compares the
vocabulary file with its pin by git object hash, so nothing is downloaded
but the page and listings.

It prints a Markdown report, and exits 1 when:

- the Note's latest version is another edition, or the page names none;
- the page links another licence, or none;
- the vocabulary file changed or is gone, or the pinned commit no longer
  holds it;
- the editors' repository states a licence;
- a check could not finish, such as a refused, failed or cut-off request,
  or an answer larger than the script reads.

A new commit that leaves the vocabulary file unchanged, and a file the
editors add beside it, are reported for information only.

Text a server chose, such as an address, a file name or an error message,
is quoted as code on one line in the report, so the issue the workflow
opens from it cannot mention anyone. A redirect is followed only to an
https address on www.w3.org or api.github.com. Set ``GITHUB_TOKEN`` to
raise the API rate limit. The token goes to api.github.com alone, never to
W3C and never on to a redirect. Usage::

    python scripts/check_upstream_release.py [--report FILE]
"""

from __future__ import annotations

import argparse
import html
import http.client
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from functools import cache
from pathlib import Path

USER_AGENT = "lmodel-void-watch"
API_HOST = "https://api.github.com/"
# The hosts a redirect may lead to: W3C's, which serves the Note's page, and
# the GitHub API's.
HOSTS = frozenset({"www.w3.org", "api.github.com"})
API = f"{API_HOST}repos/cygri/void"

# The most the script reads of one answer. The largest, the editors' file
# tree, is about 9 kB, and the Note's page about 92 kB.
MAX_BYTES = 5_000_000

# The edition of the Note the schema renders, as the date in its dated
# address, and that address, which is the schema header's `version` and
# `source`. tests/test_upstream.py holds the header and these pins equal.
# Move them together, with the header, when the schema moves to another
# edition.
PINNED_EDITION = "2011-03-03"
PINNED_SOURCE = "https://www.w3.org/TR/2011/NOTE-void-20110303/"

# The Note's latest-version address, which W3C points at the newest edition.
LATEST = "https://www.w3.org/TR/void/"

# The licence the Note's page links to as its document use rules: the W3C
# Document License, whose address now redirects to its 2023 version.
PINNED_DOCUMENT_LICENSE = "https://www.w3.org/Consortium/Legal/copyright-documents"

# The editors' repository at the commit the term list was read from, and the
# git object hash of the vocabulary file there. scripts/extract_void_terms.py
# pins the same values, and tests/test_upstream.py holds the two equal.
PINNED_COMMIT = "5b2ca68b7897c2613d4269fd725f1812dce21267"
PINNED_BLOBS = {"rdfs/void.ttl": "9a7ca133acf83628d7850b0bdff58c507a5504d4"}

# The folder whose new files are worth a reader's look.
WATCHED = ("rdfs/",)

# A licence link on a W3C page: the Consortium's legal pages or the newer
# copyright pages.
LICENCE_LINK = re.compile(
    r'href="(https?://www\.w3\.org/(?:Consortium/Legal/copyright-[\w-]+|copyright/[\w-]+/?))"'
)
DATED_VERSION = re.compile(r"/TR/(\d{4})/[A-Z]+-void-(\d{4})(\d{2})(\d{2})/?$")


class _ExpectedHostRedirect(urllib.request.HTTPRedirectHandler):
    """Follow a redirect only to an https address on one of HOSTS."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        parts = urllib.parse.urlsplit(newurl)
        if parts.scheme != "https" or parts.hostname not in HOSTS:
            raise ValueError(f"a redirect leads off the expected hosts, to {newurl}")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


# An opener in place of urlopen's, whose redirect handler follows any address.
_open = urllib.request.build_opener(_ExpectedHostRedirect).open


def _get(url: str) -> tuple[str, bytes]:
    """The address that answered, after any redirect, and the answer's body."""
    headers = {"User-Agent": USER_AGENT}
    if url.startswith(API_HOST):
        headers["Accept"] = "application/vnd.github+json"
    req = urllib.request.Request(url, headers=headers)
    token = os.environ.get("GITHUB_TOKEN")
    if token and url.startswith(API_HOST):
        # urllib copies ordinary headers onto a redirect, so the token goes in
        # an unredirected one and reaches api.github.com alone.
        req.add_unredirected_header("Authorization", f"Bearer {token}")
    with _open(req, timeout=60) as resp:
        body = resp.read(MAX_BYTES + 1)
        answered = resp.geturl()
    if len(body) > MAX_BYTES:
        raise ValueError(f"the answer from {url} is larger than {MAX_BYTES} bytes")
    return answered, body


def _json(url: str):
    return json.loads(_get(url)[1])


def _code(text: object) -> str:
    """Text a server chose, such as an address or a file name, as a code
    span on one line, so it cannot mention a person or add a link in the
    issue. A blank line would end the span, so every run of spaces and line
    breaks is one space."""
    return "`" + " ".join(str(text).replace("`", "'").split()) + "`"


def _same_address(a: str, b: str) -> bool:
    """Two W3C addresses are the same one whatever their scheme and trailing
    slash: the Note's page writes http in its text and https in its links."""

    def norm(url: str) -> str:
        return re.sub(r"^https?://", "", url).rstrip("/")

    return norm(a) == norm(b)


def _link_after(label: str, page: str) -> str | None:
    """The address a W3C page gives after a term such as "This version:"."""
    match = re.search(
        rf"<dt>\s*{re.escape(label)}\s*</dt>\s*<dd>\s*<a\s+href=\"([^\"]+)\"",
        page,
        flags=re.I,
    )
    return html.unescape(match.group(1)) if match else None


def edition_of(address: str) -> str | None:
    """The date of a dated version's address, as YYYY-MM-DD."""
    match = DATED_VERSION.search(address)
    return "-".join(match.groups()[1:]) if match else None


def check_edition() -> tuple[list[str], bool]:
    """Report whether the Note's latest version is still the pinned edition,
    and whether its page still links the pinned licence."""
    answered, body = _get(LATEST)
    page = body.decode("utf-8", "replace")
    report, attention = [], False
    if not _same_address(answered, LATEST):
        report.append(f"- {LATEST} redirected to {_code(answered)}.")
    this = _link_after("This version:", page)
    if this is None:
        attention = True
        report.append(
            f"- **{LATEST} names no dated version.** Read the page in a browser: "
            "W3C may have retired the Note or changed the page's form."
        )
    elif not _same_address(this, PINNED_SOURCE):
        attention = True
        dated = edition_of(this)
        shown = f"the edition of {dated}" if dated else "another address"
        report.append(
            f"- **The latest version of the Note is {shown}, {_code(this)}; the schema "
            f"renders {PINNED_EDITION}.** Read what changed, decide whether the schema "
            "moves to it, and move the pins here, in scripts/extract_void_terms.py "
            "and in the schema header."
        )
    else:
        report.append(
            f"- The latest version of the Note is the pinned edition, {PINNED_SOURCE}."
        )

    links = sorted(set(LICENCE_LINK.findall(page)))
    if links != [PINNED_DOCUMENT_LICENSE]:
        attention = True
        shown = ", ".join(_code(link) for link in links) if links else "no licence"
        report.append(
            f"- **The Note's page now links {shown}, not {PINNED_DOCUMENT_LICENSE}.** "
            "Read what the new terms allow and update NOTICE."
        )
    else:
        report.append(
            f"- The Note's page links the W3C Document License, {PINNED_DOCUMENT_LICENSE}."
        )
    return report, attention


@cache
def _tree(ref: str) -> dict[str, str]:
    """Every file of the editors' repository at a ref, by path, with its
    object hash. A ref the repository does not hold gives an empty mapping.
    Each tree is asked for once, and no caller changes what it returns."""
    try:
        body = _json(f"{API}/git/trees/{ref}?recursive=1")
    except urllib.error.HTTPError as err:
        if err.code in (404, 422):
            return {}
        raise
    if body.get("truncated"):
        raise OSError(f"the tree at {ref} is too large for one listing")
    return {e["path"]: e["sha"] for e in body.get("tree", []) if e["type"] == "blob"}


def _head() -> tuple[str, str]:
    """The editors' default branch and the commit it is at."""
    branch = _json(API)["default_branch"]
    commit = _json(f"{API}/commits/{branch}")["sha"]
    return branch, commit


def check_vocabulary() -> tuple[list[str], bool]:
    """Report whether the pinned commit still holds the pinned vocabulary
    file, and whether the editors' default branch changes, drops or adds a
    file beside it."""
    report = [
        f"- Pinned vocabulary file: `rdfs/void.ttl` in cygri/void at commit "
        f"`{PINNED_COMMIT[:12]}`, read into `tests/upstream/void-terms.tsv`."
    ]
    attention = False
    pinned_tree = _tree(PINNED_COMMIT)
    for name, sha in sorted(PINNED_BLOBS.items()):
        if pinned_tree.get(name) != sha:
            attention = True
            report.append(
                f"- **The pinned commit no longer holds `{name}` as the pinned blob.** "
                "Find out what happened to the editors' history before trusting the term list."
            )

    branch, commit = _head()
    latest_tree = pinned_tree if commit == PINNED_COMMIT else _tree(commit)
    for name, sha in sorted(PINNED_BLOBS.items()):
        if name not in latest_tree:
            attention = True
            report.append(
                f"- **`{name}` is gone from {_code(branch)} at commit {_code(commit[:12])}.** "
                "Find where the editors now keep the vocabulary file, and move the pins."
            )
        elif latest_tree[name] != sha:
            attention = True
            report.append(
                f"- **`{name}` changed at commit {_code(commit[:12])} on {_code(branch)}.** "
                "Read what changed, run scripts/extract_void_terms.py against the new "
                "commit, and move the pins here and in that script."
            )
    added = sorted(
        path
        for path in latest_tree
        if path.startswith(WATCHED) and path not in PINNED_BLOBS
    )
    if added:
        report.append(
            "- For information, the editors' repository also holds "
            + ", ".join(_code(n) for n in added)
            + " beside the vocabulary file."
        )
    if commit != PINNED_COMMIT and not attention:
        report.append(
            f"- For information, {_code(branch)} is at commit {_code(commit[:12])}, "
            "which leaves the vocabulary file unchanged."
        )
    elif not attention:
        report.append(f"- {_code(branch)} is still at the pinned commit.")
    return report, attention


def check_licence() -> tuple[list[str], bool]:
    """Report whether the editors' repository still states no licence.
    GitHub answers 404, or names no licence, when it detects none."""
    try:
        found = (_json(f"{API}/license").get("license") or {}).get("spdx_id")
    except urllib.error.HTTPError as err:
        if err.code != 404:
            raise
        found = None
    if found:
        return [
            f"- **The editors' repository now states a licence, {_code(found)}.** "
            "Read what it allows: it may let the vocabulary file be copied here. "
            "Update NOTICE either way."
        ], True
    return ["- The editors' repository states no licence, as pinned."], False


# Each check, by the name the report gives it when it cannot finish.
CHECKS = (
    ("edition", check_edition),
    ("vocabulary file", check_vocabulary),
    ("licence", check_licence),
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--report", type=Path, help="Also write the Markdown report to this file"
    )
    args = parser.parse_args(argv)
    lines = [f"- Pinned edition: the VoID Note of {PINNED_EDITION}, {PINNED_SOURCE}."]
    attention = False
    for label, check in CHECKS:
        try:
            found, needs = check()
        # OSError covers a refused or failed request and a timeout,
        # HTTPException and EOFError a connection cut off mid-answer,
        # ValueError an answer that is not JSON or is too large, and
        # LookupError, TypeError and AttributeError JSON of another shape.
        except (
            OSError,
            http.client.HTTPException,
            EOFError,
            ValueError,
            LookupError,
            TypeError,
            AttributeError,
        ) as err:
            found = [f"- **The {label} check could not finish: {_code(err)}.**"]
            needs = True
        lines += found
        attention = attention or needs
    text = "\n".join(lines) + "\n"
    print(text, end="")
    if args.report:
        args.report.write_text(text, encoding="utf-8")
    return 1 if attention else 0


if __name__ == "__main__":
    sys.exit(main())
