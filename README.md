# samplepackagename
Short description of your package.

[![Actions Status][actions-badge]][actions-link]
[![Documentation Status][rtd-badge]][rtd-link]

[![PyPI version][pypi-version]][pypi-link]
[![Conda-Forge][conda-badge]][conda-link]
[![PyPI platforms][pypi-platforms]][pypi-link]

[![GitHub Discussion][github-discussions-badge]][github-discussions-link]

## Template Instructions

The below steps will create a complete Python package with testing, a documentation website, and versions upload to both PyPI (pip) and Conda-Forge (conda) for each new version release in GitHub.

Steps:
1) Initiate your repository:
    - On this [template's page](https://github.com/mdtanker/python_package_template), click the `Use this template` button to `Create a new repository`.
    - choose a project name
        - for simplicity, this name will be used for all of the follow: the folder name that holds this repository as well as the code folder under `src/`, the name of the python package on both PyPI and Conda-Forge, and the repository name on GitHub. Because of these constraints, the best choice is a lowercase word with no spaces or punctuation. While capitalization and punctuation may help readability, they greatly increase the hassle during various stages of the packaging. Ensure your chosen name is available on both [PyPI](https://pypi.org/) and [Conda-Forge](https://conda-forge.org/packages/).
    - choose if you want the repository in your personal account or in one of your organization's accounts.
    - add a 1 sentence description of the package.
    - choose public or private. This can be changed later, but to be published on PyPI or Conda-Forge, or for the documentation website to work, it needs to be public.
    - create the repository
    - update any repository settings, below are my recommended settings:
        - protect the main branch so any changed to it need to be made through a Pull Request.
            - go to the repository's `Settings`, `Branches`, `Add branch ruleset`. Name it "protected_main", make the `Enforecement status` Active, include the Default branch as the target, and check the following `Rules`: `Restrict deletion`, `Require a pull request before merging`, only allow `Squash` as a merge method, and `Block force pushes`
2) Update this template:
    - clone your repository to your computer with `git clone <url of the github repo>`
    - change all instances of `samplepackagename` in this repository with your chosen name. (If use a program like VSCode use a `search and replace` function (i.e. `ctrl+f`))
        - this includes the folder name of `src/samplepackagename/`
    - replace all instances of `yourname` with your name
        - your name can be "Maintainers of <samplepackagename>" if there are multiple people.
    - replace all instances of `organizationname` with your GitHub organization (or personal) account name.
    - update `pyproject.yml` with a description and keywords
    - add a description of your project here in the README, as well as in `docs/index.md`.
    - add your info to `AUTHORS.md`
    - at this point, it might be good to make your initial commit to your repository with the following git commands:
        ```bash
        git checkout -b new-branch
        git add .
        git commit -m "initialize template with names"
        git push -u origin new-branch
        ```
    - in your GitHub repository, go to the `Pull request` tab and open a PR for your changes. Merge this into main.
3) Add your code
    - pull in your above changes with `git fetch` and `git pull`.
    - decide on a module name(s)
        - these need to be lowercase, should be short and while possible, shouldn't include underscores.
        - if your package is going to be small, a single module with the same name as the package is fine. If it's going to be more than a few hundred lines of code, it's best to separate your code into distinct modules which perform similar tasks. - for each module you want do the following:
            - create / rename the existing file: `src/samplepackagename/module1.py`
            - create / rename the test file: `tests/test_module1.py`
            - add a description of the module to `docs/overview.md`
            - replace all instances of `module1` with your module's name.
    - add your code to your module `.py` files.
    - you have two options for how users can import your code.
        1) ```python
            from samplepackagename import module1

            module1.function1()
            ```
            - this option is available by default for any functions you write, and is nice if you have several modules because it clearly shows where the code is coming from.
        2) ```python
            import samplepackagename

            samplepackagename.function1()
            ```
            - to allow `function1` to be imported as above, you need to manually add it to the list in `src/samplepackagename/_init_.py`. If you only have 1 module, this may be a better technique.
    - add tests for your modules' test file in `tests/`.
4) Specify your dependencies
    - dependencies for your package should typically only be those that are directly used (imported) in your source code (or are explicitly needed but not import), but not the dependencies of your dependencies. If you use a package in your documentation, but not in the source code, include this as an _optional_ dependency. If you have a portion of your code that some users may not utilize, such as visualization functions, the dependencies you require for that, such as matplotlib, can also be include as _optional_ dependencies to reduces the constraints for users who don't require it.
    - core dependencies are specified in `pyproject.toml` under the `[project]` section with the format `dependencies = ["pandas", "scipy>=1.0"]`.
    - optional dependencies are specified in `pyproject.toml` under the `[dependency-groups]` section with the following format, for example for optional documentation dependencies: `docs = ["sphinx>=7.0",]`.
    - Dependency version's should only be constrained to specific versions if you know there is an issue, and they should almost never be pinned to specific versions, as this will cause many issues for anyone who wants to use your package in their own environments.
    - this template also includes files and commands to create `conda` environments. These are used both in developing, and in GitHub automations. You need to manually ensure the dependencies listed in `environmental.yml` match those in `pyproject.toml`. Include all optional dependencies in the `environmental.yml`. If a dependency is only available via pip, and not conda, add it at the bottom to be installed via pip.
5) Create environment, style check, test, and commit your changes.
    - follow the instructions in `CONTRIBUTING.md` starting at section `Setting up nox` and stopping before `Publish a new release`.
    - these steps should result in a merged PR with your code.
6) Set up automated Zenodo releases
    - if you haven't already, link your organization (or personal) GitHub account to [Zenodo](https://zenodo.org/) using `Linked accounts` under your Zenodo profile.
    - do to the `GitHub` menu on your Zenodo profile.
    - click the Sync button and then turn on the switch for your repository.
    - any future GitHub releases should now result in a new Zenodo release automatically.
7) Set up publishing on TestPyPI
    - before publishing to the real PyPI, we will publish to Test-PyPI to ensure everything works .
    - make an account on [TestPyPI](https://test.pypi.org/).
    - under 'Your Projects', and 'Publishing', 'Add a new pending publisher', fill out your info.
        - the project name and repository name should be what you chose for `samplepackagename`.
        - the owner should be what you used from `organizationname`.
        - Workflow name should be `cd.yml`
        - Environment name should be `pypi`
    - note that this doesn't reserve your package name until you make your first actual release!
8) Make a GitHub release
    - On the main GitHub page, on the right side click `Create a new release`.
    - click `Select tag` and type `v0.0.1`.
    - set a Release title: "Initial release"
    - click `Publish release`
    - this should automatically trigger a few things:
        1) a DOI will be added to your Zenodo, add this DOI to `docs/citing.md`.
        2) the GitHub action `CD` should be triggered, create a release of `v0.0.1` to TestPyPI.
            - to test this worked correctly, run the below commands to create a new conda environment using the TestPiPI release, and run your codes tests.
            ```bash
            mamba  create --name test_pypi python
            mamba activate test_pypi
            pip install -i https://test.pypi.org/simple/ samplepackagename
            nox -s test
            ```
9) Make a PyPI (pip) release
    - If the install and test above worked then we can change from TestPyPI to normal PyPI.
    - in `.github/workflows/cd.yml` comment out or delete the last line: `repository-url: https://test.pypi.org/legacy/`. Now any future reruns of this action will release to PyPI.
    - In this case, since the GitHub release has already been made, we need to manually trigger the `CD` workflow in GitHub.
        - At [this link](https://github.com/mdtanker/python_package_template/actions/workflows/cd.yml), click the `Run workflow` button.
        - This should build the package and release it to PyPI.
10) Set up publishing on Conda-Forge
    - create a conda-forge feedstock
11) Set up ReadTheDocs for the documentation website
    - log into ReadTheDocs using your GitHub account.
    - click `Add project` and ssearch for your repository.
    - Chose your project name, ideally its the same as your package name, but it doesn't have to be. If it's different, update the badge below: `[rtd-link]: https://samplepackagename.readthedocs.io/en/latest/?badge=latest`
    - Go to `settings` to update anything you'd like
        - check `Build pull requests for this project`.
    - for each commit to main, ReadTheDocs should automatically update the documentation website. Also, in PR's there should be a link to view the new docs to check them before merging the PR.
12) Finalize
    - remove all the above instructions and raise any issues in this template's repository if you have any suggestion or found any errors in this template!

<!-- SPHINX-START-badges -->

<!-- prettier-ignore-start -->
[actions-badge]:            https://github.com/organizationname/samplepackagename/workflows/CI/badge.svg
[actions-link]:             https://github.com/organizationname/samplepackagename/actions
[conda-badge]:              https://img.shields.io/conda/vn/conda-forge/samplepackagename
[conda-link]:               https://github.com/conda-forge/samplepackagename-feedstock
[github-discussions-badge]: https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github
[github-discussions-link]:  https://github.com/organizationname/samplepackagename/discussions
[pypi-link]:                https://pypi.org/project/samplepackagename/
[pypi-platforms]:           https://img.shields.io/pypi/pyversions/samplepackagename
[pypi-version]:             https://img.shields.io/pypi/v/samplepackagename
[rtd-badge]:                https://readthedocs.org/projects/samplepackagename/badge/?version=latest
[rtd-link]:                 https://samplepackagename.readthedocs.io/en/latest/?badge=latest

<!-- prettier-ignore-end -->

<!-- SPHINX-END-badges -->
