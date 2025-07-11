from __future__ import annotations

from samplepackagename import logger  # pylint: disable=unused-import

# Any functions or classes defined here which you want to be available when to users
# with `import samplepackagename` should be added to the list in `__init__.py`.


def example_function() -> str:
    """
    An example function that can be imported from the project.

    Returns
    -------
    str
        A simple greeting message.
    """
    logger.info("This is an example function.")
    return "Hello from example_function!"
