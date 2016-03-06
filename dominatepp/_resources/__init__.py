import os
import sys
from pathlib import Path


def get_resource(path: Path) -> Path:
    """
    :param path: relative to the resources directory
    :return: absolute resource path
    """
    module_dir = os.path.dirname(sys.modules['dominatepp'].__file__)
    return Path(module_dir).joinpath('_resources').joinpath(path).absolute()


def load_resource(path: Path) -> bytes:
    with get_resource(path).open('rb') as fo:
        return fo.read()
