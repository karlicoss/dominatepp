from .helpers import assert_same_html

from unittest import TestCase
import dominatepp


class TestMisc(TestCase):
    def test_stylesheet(self):
        path = "http://whatever.com/stylesheet.css"
        expected = '<link href="http://whatever.com/stylesheet.css" rel="stylesheet"/>'
        actual = dominatepp.stylesheet(path).render()
        assert_same_html(self, actual, expected)

    def test_a_link(self):
        url = "http://whatever.com/document.html"
        text = "A link to whatever you wish!"
        expected = '<a href="http://whatever.com/document.html">A link to whatever you wish!</a>'
        actual = dominatepp.a_link(text, url).render()
        assert_same_html(self, actual, expected)
