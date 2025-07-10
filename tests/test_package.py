from __future__ import annotations

import importlib.metadata

import packagename


def test_version():
    assert importlib.metadata.version("packagename") == packagename.__version__
