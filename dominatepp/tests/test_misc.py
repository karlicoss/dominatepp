import tempfile

import shutil

from pathlib import Path

from .helpers import assert_same_html
from unittest import TestCase
import dominatepp


class TestMisc(TestCase):
    def setUp(self):
        self.test_dir = Path(tempfile.mkdtemp())

    def tearDown(self):
        shutil.rmtree(self.test_dir.as_posix())

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

    def test_inline_script_from(self):
        script_file = self.test_dir.with_name('test_script.js')
        with script_file.open('w') as fo:
            fo.write(
                """
                    var x = 10;
                    x += 5;
                    document.getElementById("demo").innerHTML = x;
                """
            )
        expected = '<script>var x = 10; x += 5; document.getElementById("demo").innerHTML = x; </script>'
        actual = dominatepp.inline_script_from(script_file).render()
        assert_same_html(self, actual, expected)

    def test_inline_script(self):
        script = """
                    var x = 10;
                    x += 5;
                    document.getElementById("demo").innerHTML = x;
                 """
        expected = '<script>var x = 10; x += 5; document.getElementById("demo").innerHTML = x; </script>'
        actual = dominatepp.inline_script(script).render()
        assert_same_html(self, actual, expected)
