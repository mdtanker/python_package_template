# ruff: noqa: F401, E402


import logging

from ._version import version as __version__

__all__ = ["__version__"]


logger = logging.getLogger(__name__)

from .module1 import (
    # List of functions and classes to be imported when using `import samplepackagename`
    example_function,
)
