from unittest import TestCase

from html5print import HTMLBeautifier


def assert_same_html(asserter: TestCase, actual: str, expected: str):
    """
        Tests whether two HTML strings are 'equivalent'
    """
    html1 = HTMLBeautifier.beautify(actual)
    html2 = HTMLBeautifier.beautify(expected)
    asserter.assertMultiLineEqual(html1, html2)
