# packagename
Short description of your package.

[![Actions Status][actions-badge]][actions-link]
[![Documentation Status][rtd-badge]][rtd-link]

[![PyPI version][pypi-version]][pypi-link]
[![Conda-Forge][conda-badge]][conda-link]
[![PyPI platforms][pypi-platforms]][pypi-link]

[![GitHub Discussion][github-discussions-badge]][github-discussions-link]

## Template Instructions
Steps:
1) choose a project name (no spaces, capitals or underscores).
    - change all instances of `packagename` in this repository with your chosen name. (use a `search and replace` function (i.e. `ctrl+f`))
    - this includes the folder name of `src/packagename/`
2) replace all instance of `yourname` with your name
    - your name can be "Maintainers of <packagename>" if there are multiple people.
3) replace all instance of `organizationname` with your GitHub organization (or personal) account name
4) add your pip/conda dependencies to `environmental.yml` and `pyproject.toml` in the dependency section.
5) update `pyproject.yml`
    - add a description
    - add keywords
6) add your code to and rename `src/packagename/module1.py`
7) add any functions you want available on import to the list in `src/packagename/_init_.py`
8) add tests for `module1.py` to `tests/test_module1.py` and rename to your module
9) remove all the above instructions and add a description of your project here, and tweak the below user instructions as needed

<!-- SPHINX-START-badges -->

<!-- prettier-ignore-start -->
[actions-badge]:            https://github.com/organizationname/packagename/workflows/CI/badge.svg
[actions-link]:             https://github.com/organizationname/packagename/actions
[conda-badge]:              https://img.shields.io/conda/vn/conda-forge/packagename
[conda-link]:               https://github.com/conda-forge/packagename-feedstock
[github-discussions-badge]: https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github
[github-discussions-link]:  https://github.com/organizationname/packagename/discussions
[pypi-link]:                https://pypi.org/project/packagename/
[pypi-platforms]:           https://img.shields.io/pypi/pyversions/packagename
[pypi-version]:             https://img.shields.io/pypi/v/packagename
[rtd-badge]:                https://readthedocs.org/projects/packagename/badge/?version=latest
[rtd-link]:                 https://packagename.readthedocs.io/en/latest/?badge=latest

<!-- prettier-ignore-end -->

<!-- SPHINX-END-badges -->


## Getting the code

You can download a copy of all the files for this project by cloning the GitHub repository:

    git clone https://github.com/organizationname/packagename

## Dependencies

These instructions assume you have `Make` installed. If you don't you can just open up the `Makefile` file and copy and paste the commands into your terminal. This also assumes you have Python installed.

Install the required dependencies with either `conda` or `mamba`:

    cd packagename

    make create

Activate the newly created environment:

    mamba activate packagename

Install the local project

    make install


## How to use

To use this code, you need to first import the package. There are two options:

### 1: Import the main package

For example:
```python
import packagename
```

will allow you to access the function `example_function()` with either `packagename.module1.example_function()` or just `packagename.example_function()`.

Functions accessed in this way need to be explicitly added to the file `src/packagename/__init__.py`

### 2: Import each module individually

For example:
```python
from packagename import module1
```
Will allow you to access the function `example_function()` with `module1.example_function()`.

## Developer instructions

Style-check your code:

    nox -s style

This will run both of the below, which you can do individually as well:

    nox -s lint
    nox -s pylint

Test your code

    nox -s test

If you need to change the dependencies of the package, either adding, removing, or adding version constraints, you need to do this in both `environment.yml` and `pyproject.toml`. Then with your conda environment activated run:

    make update

When writing code; use logging to inform users of info, errors, and warnings. In each module `.py` file, import the project-wide logger instance with `from packagename import logger` and then for example: `logger.info("log this message")`

Build the documentation and check locally:

    nox -s docs
