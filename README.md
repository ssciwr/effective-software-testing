# Welcome to Effective Software Testing

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/ssciwr/effective-software-testing/ci.yml?branch=main)](https://github.com/ssciwr/effective-software-testing/actions/workflows/ci.yml)
[![Documentation Status](https://readthedocs.org/projects/effective-software-testing/badge/)](https://effective-software-testing.readthedocs.io/)
[![codecov](https://codecov.io/gh/ssciwr/effective-software-testing/branch/main/graph/badge.svg)](https://codecov.io/gh/ssciwr/effective-software-testing)

## Installation

The Python packaage `effectivesoftwaretesting` can be installed from PyPI:

```
python -m pip install effectivesoftwaretesting
```

## Development installation

If you want to contribute to the development of `effectivesoftwaretesting`, we recommend
the following editable installation from this repository:

```
git clone git@github.com:ssciwr/effective-software-testing.git
cd effective-software-testing
python -m pip install --editable .[tests]
```

Having done so, the test suite can be run using `pytest`:

```
python -m pytest
```

## Acknowledgments

This repository was set up using the [SSC Cookiecutter for Python Packages](https://github.com/ssciwr/cookiecutter-python-package).
