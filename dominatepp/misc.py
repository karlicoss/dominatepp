import dominate.tags as T


def stylesheet(path: str) -> T.link:
    return T.link(rel='stylesheet', href=path)


def a_link(text: str, url: str) -> T.a:
    return T.a(text, href=url)
