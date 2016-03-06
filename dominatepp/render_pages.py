from pathlib import Path

from dominate import tags as T
from dominate import tags  # extra import for intellij type hints. It can't parse T.html_tag
from typing import List

from dominatepp import inline_script_from, stylesheet
from dominatepp._resources import get_resource, load_resource

ID_CONTAINER = 'container'

_PAGE_FRAME = 'page_frame'
_JQUERY_URL = "https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"
_NAVBAR_CSS = 'navbar.css'
_STYLE_CSS = 'style.css'
_PAGE_CSS = 'page.css'
_SELECTED_JS = 'selected.js'


class PagesRenderer(object):
    """
    :type rendered_items: list[tags.html_tag]
    :type pages: dict[str, tags.html]
    :type resources: dict[str, bytes]
    """

    def __init__(self, rendered_items: List[T.html_tag], page_css: bytes=None):
        super().__init__()
        self.rendered_items = rendered_items
        self.pages = {}
        self.resources = {
            _NAVBAR_CSS: load_resource(Path(_NAVBAR_CSS)),
            _STYLE_CSS: load_resource(Path(_STYLE_CSS)),
            _PAGE_CSS: page_css if page_css is not None else b'',
        }

    def render(self, posts_per_page=25):
        pages_count = (len(self.rendered_items) + posts_per_page - 1) // posts_per_page
        page_names = ["%d.html" % i for i in range(pages_count)]

        nav_section = T.nav(
            *[T.a(str(i), href=page_names[i], target=_PAGE_FRAME) for i in range(pages_count)]
        )

        index = T.html(
            T.head(
                T.meta(charset='utf-8'),
                stylesheet(_STYLE_CSS),
                stylesheet(_NAVBAR_CSS),
                T.script(src=_JQUERY_URL),
                inline_script_from(get_resource(Path(_SELECTED_JS)))
            ),
            T.body(
                nav_section,
                T.iframe(name=_PAGE_FRAME, src=page_names[0] if pages_count > 0 else 'none', width='100%', height='100%', style='border:none')
            )
        )
        self.pages['index.html'] = index

        for page_index in range(pages_count):
            page_items = self.rendered_items[page_index * posts_per_page: (page_index + 1) * posts_per_page]
            chunk_html = T.html(
                T.head(stylesheet('page.css')),
                T.body(
                    T.div(*page_items, id=ID_CONTAINER)
                )
            )
            self.pages[page_names[page_index]] = chunk_html

    def save_to(self, html_path: Path):
        for name, data in self.resources.items():
            with html_path.joinpath(name).open('wb') as fo:
                fo.write(data)

        for name, html in self.pages.items():
            with html_path.joinpath(name).open('w') as fo:
                fo.write(html.render())
