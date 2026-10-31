"""Checks the upstream watch's decisions against stubbed answers.

scripts/check_upstream_release.py reads the VoID Note's latest-version page
and asks the GitHub API about the editors' repository. These tests replace
its one network call, `_get`, with a table of answers, so they run offline.
They show what the report says in each case the watch knows: a new edition,
a changed licence, a changed, dropped or added file, a moved branch, and a
check that could not finish.
"""

import http.client
import importlib.util
import json
import urllib.error
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "check_upstream_release.py"

# The Note's page cut down to what the watch reads: the dated version after
# "This version:" and the licence link. The words around them are this
# test's own.
PAGE = """<html><body><dl>
<dt>This version:</dt>
<dd><a href="https://www.w3.org/TR/2011/NOTE-void-20110303/">dated</a></dd>
<dt>Latest version:</dt>
<dd><a href="https://www.w3.org/TR/void/">latest</a></dd>
</dl>
<p class="copyright"><a href="https://www.w3.org/Consortium/Legal/ipr-notice#Copyright">c</a>
<a href="https://www.w3.org/Consortium/Legal/copyright-documents">document use</a></p>
</body></html>"""
NEWER_PAGE = PAGE.replace("2011/NOTE-void-20110303", "2027/NOTE-void-20270101")
OTHER_LICENCE_PAGE = PAGE.replace(
    "Consortium/Legal/copyright-documents", "copyright/software-license-2023/"
)

NEW_COMMIT = "1" * 40


@pytest.fixture
def watch():
    """A fresh copy of the script, so no test sees another's stub."""
    spec = importlib.util.spec_from_file_location("watch_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _tree(files):
    return {
        "truncated": False,
        "tree": [{"path": p, "type": "blob", "sha": s} for p, s in files.items()],
    }


def _answers(watch, page=PAGE, head=None, latest_files=None, pinned_files=None):
    """The answers of an unchanged upstream, with the parts a test changes."""
    head = head or watch.PINNED_COMMIT
    pinned_files = (
        dict(watch.PINNED_BLOBS, **{"README.md": "a" * 40})
        if pinned_files is None
        else pinned_files
    )
    answers = {
        watch.LATEST: page,
        watch.API: {"default_branch": "master"},
        f"{watch.API}/commits/master": {"sha": head},
        f"{watch.API}/license": urllib.error.HTTPError(
            f"{watch.API}/license", 404, "Not Found", None, None
        ),
        f"{watch.API}/git/trees/{watch.PINNED_COMMIT}?recursive=1": _tree(pinned_files),
    }
    if head != watch.PINNED_COMMIT:
        files = pinned_files if latest_files is None else latest_files
        answers[f"{watch.API}/git/trees/{head}?recursive=1"] = _tree(files)
    return answers


def _stub(watch, answers):
    """Make `_get` answer from the table: an exception is raised, a pair is
    the address that answered and its body, a dict is JSON and a string is a
    page at the address asked."""

    def get(url):
        answer = answers[url]
        if isinstance(answer, Exception):
            raise answer
        if isinstance(answer, tuple):
            return answer[0], answer[1].encode()
        if isinstance(answer, dict):
            return url, json.dumps(answer).encode()
        return url, answer.encode()

    watch._get = get


def _run(watch, tmp_path):
    report = tmp_path / "report.md"
    code = watch.main(["--report", str(report)])
    return code, report.read_text(encoding="utf-8")


def test_nothing_changed(watch, tmp_path):
    """With the pinned edition, licence and file, the watch exits 0."""
    _stub(watch, _answers(watch))
    code, text = _run(watch, tmp_path)
    assert code == 0, text
    assert "latest version of the Note is the pinned edition" in text
    assert "links the W3C Document License" in text
    assert "`master` is still at the pinned commit." in text
    assert "states no licence, as pinned" in text


def test_a_newer_edition(watch, tmp_path):
    """A latest version dated after the pin needs attention."""
    _stub(watch, _answers(watch, page=NEWER_PAGE))
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**The latest version of the Note is the edition of 2027-01-01" in text
    assert "the schema renders 2011-03-03.**" in text


def test_a_page_without_a_dated_version(watch, tmp_path):
    """A page that names no dated version needs a reader."""
    _stub(watch, _answers(watch, page="<html><title>Just a moment...</title></html>"))
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "names no dated version.**" in text
    assert "now links no licence" in text


def test_another_licence(watch, tmp_path):
    """A licence link other than the W3C Document License needs attention."""
    _stub(watch, _answers(watch, page=OTHER_LICENCE_PAGE))
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "now links `https://www.w3.org/copyright/software-license-2023/`" in text


def test_the_vocabulary_file_changed(watch, tmp_path):
    """A new blob for the vocabulary file at the branch's head needs attention."""
    changed = {"rdfs/void.ttl": "b" * 40}
    _stub(watch, _answers(watch, head=NEW_COMMIT, latest_files=changed))
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**`rdfs/void.ttl` changed at commit `111111111111` on `master`.**" in text


def test_the_vocabulary_file_is_gone(watch, tmp_path):
    """A head without the vocabulary file needs attention."""
    _stub(watch, _answers(watch, head=NEW_COMMIT, latest_files={"README.md": "a" * 40}))
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**`rdfs/void.ttl` is gone from `master` at commit `111111111111`.**" in text


def test_the_pinned_commit_lost_the_file(watch, tmp_path):
    """A pinned commit that no longer holds the pinned blob needs attention."""
    _stub(watch, _answers(watch, pinned_files={}))
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**The pinned commit no longer holds `rdfs/void.ttl`" in text


def test_a_new_commit_and_an_added_file_are_for_information(watch, tmp_path):
    """A new head that keeps the file, and a file added beside it, are
    reported and leave the exit code at 0."""
    files = dict(watch.PINNED_BLOBS, **{"rdfs/void-2.ttl": "c" * 40})
    _stub(watch, _answers(watch, head=NEW_COMMIT, latest_files=files))
    code, text = _run(watch, tmp_path)
    assert code == 0, text
    assert "also holds `rdfs/void-2.ttl` beside the vocabulary file." in text
    assert (
        "`master` is at commit `111111111111`, which leaves the vocabulary file unchanged."
        in text
    )


def test_the_editors_state_a_licence(watch, tmp_path):
    """A licence GitHub detects in the editors' repository needs attention."""
    answers = _answers(watch)
    answers[f"{watch.API}/license"] = {"license": {"spdx_id": "CC-BY-4.0"}}
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**The editors' repository now states a licence, `CC-BY-4.0`.**" in text


@pytest.mark.parametrize(
    ("failure", "shown"),
    [
        (
            urllib.error.HTTPError("https://x", 403, "Forbidden", None, None),
            "`HTTP Error 403",
        ),
        (urllib.error.URLError("Connection refused"), "`<urlopen error"),
        (http.client.IncompleteRead(b"<html>"), "`IncompleteRead"),
        (EOFError("cut"), "`cut`"),
        (LookupError("unknown encoding: x-bogus"), "`unknown encoding"),
        (
            ValueError("the answer is larger than 5000000 bytes"),
            "`the answer is larger",
        ),
    ],
)
def test_a_check_that_could_not_finish(watch, tmp_path, failure, shown):
    """A refused, failed, cut-off or oversized answer stops one check, says
    so, and leaves the other checks to run and the report to be written."""
    answers = _answers(watch)
    answers[watch.LATEST] = failure
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert f"**The edition check could not finish: {shown}" in text
    assert "states no licence, as pinned" in text


def test_json_of_another_shape_could_not_finish(watch, tmp_path):
    """An API answer without the keys the watch reads is a check that could
    not finish, not a crash."""
    answers = _answers(watch)
    answers[watch.API] = {"message": "moved"}
    answers[f"{watch.API}/license"] = {"license": "not an object"}
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**The vocabulary file check could not finish: `'default_branch'`.**" in text
    assert "**The licence check could not finish: `" in text


def test_a_json_list_where_an_object_belongs_could_not_finish(watch, tmp_path):
    """An API answer that is a list, where the watch reads an object's key,
    raises a TypeError, which is a check that could not finish."""
    answers = _answers(watch)
    answers[watch.API] = (watch.API, '["master"]')
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**The vocabulary file check could not finish: `list indices" in text
    assert "states no licence, as pinned" in text


def test_a_truncated_tree_could_not_finish(watch, tmp_path):
    """A file listing GitHub cut short cannot show the vocabulary file is
    unchanged, so the check says it could not finish."""
    answers = _answers(watch)
    answers[f"{watch.API}/git/trees/{watch.PINNED_COMMIT}?recursive=1"] = {
        "truncated": True,
        "tree": [],
    }
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**The vocabulary file check could not finish: `the tree at" in text
    assert "too large for one listing`.**" in text


def test_a_redirect_is_reported_and_quoted(watch, tmp_path):
    """The address that answered is named, as code, when it is not the one
    asked, and a backtick in it cannot end the quotation."""
    answers = _answers(watch)
    answers[watch.LATEST] = ("https://www.w3.org/TR/@someone`x", PAGE)
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 0, text
    assert "redirected to `https://www.w3.org/TR/@someone'x`." in text


def test_text_the_server_chose_is_quoted(watch, tmp_path):
    """A dated address on the page is quoted as code, so it cannot mention a
    person in the issue."""
    page = PAGE.replace(
        "https://www.w3.org/TR/2011/NOTE-void-20110303/", "https://example.org/@someone"
    )
    _stub(watch, _answers(watch, page=page))
    text = _run(watch, tmp_path)[1]
    assert "is another address, `https://example.org/@someone`;" in text


class _Answer:
    def __init__(self, url):
        self.url = url

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def geturl(self):
        return self.url

    def read(self, size):
        return b"{}"


def test_the_token_goes_to_the_api_alone(watch, monkeypatch):
    """The token travels in an unredirected header to api.github.com, and
    never to W3C."""
    monkeypatch.setenv("GITHUB_TOKEN", "not-to-leak")
    sent = {}

    def urlopen(req, timeout):
        sent[req.full_url] = (dict(req.header_items()), dict(req.unredirected_hdrs))
        return _Answer(req.full_url)

    monkeypatch.setattr(watch, "_open", urlopen)
    watch._get(watch.API)
    watch._get(watch.LATEST)
    headers, unredirected = sent[watch.API]
    assert unredirected["Authorization"] == "Bearer not-to-leak"
    assert sent[watch.API][0]["User-agent"] == "lmodel-void-watch"
    w3c_headers, w3c_unredirected = sent[watch.LATEST]
    assert "Authorization" not in w3c_headers and not w3c_unredirected
    assert set(w3c_headers) == {"User-agent"}


def test_an_answer_over_the_cap_is_refused(watch, monkeypatch):
    """An answer larger than MAX_BYTES raises rather than being read whole."""

    class Big(_Answer):
        def read(self, size):
            return b"x" * size

    monkeypatch.setattr(watch, "_open", lambda req, timeout: Big(req.full_url))
    with pytest.raises(ValueError, match="larger than"):
        watch._get(watch.LATEST)


def test_edition_of_reads_a_dated_address(watch):
    """The date of a dated version comes from its address."""
    assert watch.edition_of(watch.PINNED_SOURCE) == watch.PINNED_EDITION
    assert watch.edition_of("https://www.w3.org/TR/void/") is None


def test_server_text_stays_on_one_line(watch, tmp_path):
    """A licence name with a blank line and a mention in it stays inside its
    code span, so the issue mentions no one."""
    answers = _answers(watch)
    answers[f"{watch.API}/license"] = {"license": {"spdx_id": "MIT\n\n@someone `x`"}}
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "now states a licence, `MIT @someone 'x'`.**" in text


def test_a_redirect_off_the_expected_hosts_is_refused(watch):
    """A redirect is followed to W3C's and the GitHub API's hosts over https,
    and to no other address."""
    handlers = watch._open.__self__.handlers
    assert any(isinstance(h, watch._ExpectedHostRedirect) for h in handlers)
    handler = watch._ExpectedHostRedirect()
    req = watch.urllib.request.Request(watch.LATEST)
    for newurl in (
        "https://example.org/TR/void/",
        "http://www.w3.org/TR/void/",
        "https://www.w3.org.example.org/TR/void/",
        "https://raw.githubusercontent.com/cygri/void/master/rdfs/void.ttl",
    ):
        with pytest.raises(ValueError, match="leads off the expected hosts"):
            handler.redirect_request(req, None, 302, "Found", {}, newurl)
    for moved in (
        "https://www.w3.org/TR/void-2/",
        "https://api.github.com/repositories/1/license",
    ):
        assert (
            handler.redirect_request(req, None, 301, "Moved", {}, moved).full_url
            == moved
        )


def test_a_refused_redirect_could_not_finish(watch, tmp_path):
    """A redirect the watch refuses stops that check, and the report quotes
    the address it was sent to."""
    answers = _answers(watch)
    answers[watch.LATEST] = ValueError(
        "a redirect leads off the expected hosts, to https://example.org/@someone"
    )
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert (
        "**The edition check could not finish: `a redirect leads off the expected "
        "hosts, to https://example.org/@someone`.**" in text
    )
