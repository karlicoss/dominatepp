import dominate.tags as T
from pathlib import Path


def stylesheet(path: str) -> T.link:
    return T.link(rel='stylesheet', href=path)


def a_link(text: str, url: str) -> T.a:
    return T.a(text, href=url)


def inline_script_from(path: Path) -> T.script:
    with path.open('r') as fo:
        return inline_script(fo.read())


def inline_script(script: str) -> T.script:
    s = T.script()
    s.add_raw_string(script)
    return s
