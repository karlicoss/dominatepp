from unittest import TestCase

from bs4 import BeautifulSoup
from html5print import HTMLBeautifier


def assert_same_html(asserter: TestCase, actual: str, expected: str):
    """
        Tests whether two HTML strings are 'equivalent'
    """
    bactual = HTMLBeautifier.beautify(actual)
    bexpected = HTMLBeautifier.beautify(expected)
    asserter.assertMultiLineEqual(bactual, bexpected)


def normalise_html(html: str) -> str:
    # default parser tries to 'fix' html, we don't want that to happen...
    prettified = BeautifulSoup(html, 'html.parser').prettify()
    # and now.. strip the spaces before newlines
    return '\n'.join([s.lstrip(' ') for s in prettified.split('\n')])


def assert_contains_html(asserter: TestCase, html: str, chunk: str):
    # indent=0: meh, but that kinda works and results in pretty assertion failures!
    bhtml = normalise_html(html)
    bchunk = normalise_html(chunk)
    asserter.assertTrue(bchunk in bhtml)  # TODO assertContainsSubstring?
