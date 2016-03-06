import shutil
import tempfile
from pathlib import Path
from unittest import TestCase

import dominate.tags as T

import dominatepp
from .helpers import assert_contains_html


class TestMisc(TestCase):
    def setUp(self):
        self.test_dir = Path(tempfile.mkdtemp())

    def tearDown(self):
        shutil.rmtree(self.test_dir.as_posix())

    def test_render_single_page(self):
        renderer = dominatepp.PagesRenderer([T.article('item1'), T.article('item2')])
        renderer.render(posts_per_page=5)
        pages = renderer.pages
        self.assertEqual(len(pages), 2)  # index + remaining
        self.assertDictContains(pages, 'index.html')
        self.assertDictContains(pages, '0.html')
        page0 = pages['0.html'].render()
        assert_contains_html(self, page0, "<article>item1</article>")
        assert_contains_html(self, page0, "<article>item2</article>")

    def test_render_multipage(self):
        renderer = dominatepp.PagesRenderer([
            T.article('item1'),
            T.article('item2'),
            T.article('item3'),
            T.article('item4'),
        ])
        renderer.render(posts_per_page=2)
        pages = renderer.pages
        self.assertEqual(len(pages), 3)  # index + 2 pages
        self.assertDictContains(pages, 'index.html')
        self.assertDictContains(pages, '0.html')
        self.assertDictContains(pages, '1.html')
        page0 = pages['0.html'].render()
        assert_contains_html(self, page0, "<article>item1</article>")
        assert_contains_html(self, page0, "<article>item2</article>")
        page1 = pages['1.html'].render()
        assert_contains_html(self, page1, "<article>item3</article>")
        assert_contains_html(self, page1, "<article>item4</article>")

    def test_save_multipage(self):
        renderer = dominatepp.PagesRenderer(
            [
                T.article('item1'),
                T.article('item2'),
                T.article('item3'),
                T.article('item4'),
            ],
            page_css=b'h { color: red; }',
        )
        renderer.render(posts_per_page=2)
        renderer.save_to(self.test_dir)
        self.assertPathExists(self.test_dir.joinpath('index.html'))
        self.assertPathExists(self.test_dir.joinpath('0.html'))
        self.assertPathExists(self.test_dir.joinpath('1.html'))
        self.assertPathExists(self.test_dir.joinpath('page.css'))

    def assertDictContains(self, dictionary, element):
        self.assertTrue(element in dictionary)

    def assertPathExists(self, path: Path):
        self.assertTrue(path.exists())  # TODO proper assert
