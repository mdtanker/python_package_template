# Install

## Online usage (Binder)

See below for the full installation instructions.
If instead you'd like to use this package online, without needing to install anything, check out our [Binder link](https://mybinder.org/v2/gh/organizationname/packagename/main), which gives full access the the package in an online environment.

This Binder environment can also be accessed by clicking the Binder icon in any of the `gallery` or `tutorial` examples.

## Install Python

Before installing _packagename_, ensure you have Python 3.9 or greater downloaded.
If you don't, we recommend setting up Python with Miniforge.
See the install instructions [here](https://github.com/conda-forge/miniforge).

## Install _packagename_ Locally

There are 3 main ways to install `packagename`. We show them here in order of simplest to hardest.

### Conda / Mamba

```{note}
`conda` and `mamba` are interchangeable
```

The easiest way to install this package and it's dependencies is with conda or mamba into a new virtual environment:

    mamba create --name packagename --yes --force packagename --channel conda-forge

Activate the environment:

    mamba activate packagename

### Pip

Instead, you can use pip to install `packagename`, but first you maybe need to install a few dependencies first with conda.
This is because a few dependencies rely on C packages, which can only be install with conda/mamba and not with pip.

Create a new virtual environment:

```
mamba create --name packagename --yes --force <<add conda packages here>> --channel conda-forge
```

activate the environment and use `pip` to install `packagename`:

```
conda activate packagename
pip install packagename
```

```{note}
to install the optional dependencies, use this instead:
`pip install packagename[all]`
```

### Development version

You can use pip, with the above created environment, to install the latest source from GitHub:

    pip install git+https://github.com/organizationname/packagename.git

Or you can clone the git repository and install:


    git clone https://github.com/organizationname/packagename.git
    cd packagename
    pip install .

## Test your install

Run the following inside a Python interpreter:

```python
import packagename

packagename.__version__
```

This should tell you which version was installed.

To further test, you can clone the GitHub repository and run the suite of tests, see the [Contributors Guide](https://packagename.readthedocs.io/en/latest/contributing.html).

A simpler method to ensure the basics are working would be to download any of the jupyter notebooks from the documentation and run them locally. On the documentation, each of the examples should have a drop down button in the top right corner to download the `.ipynb`.
