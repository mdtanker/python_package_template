import importlib.metadata

import samplepackagename


def test_version():
    assert (
        importlib.metadata.version("samplepackagename") == samplepackagename.__version__
    )
