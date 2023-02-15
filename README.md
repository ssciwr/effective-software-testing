# Effective Software Testing

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/ssciwr/effective-software-testing/ci.yml?branch=main)](https://github.com/ssciwr/effective-software-testing/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/ssciwr/effective-software-testing/branch/main/graph/badge.svg)](https://codecov.io/gh/ssciwr/effective-software-testing)

A sample Python project to accompany the SSC compact course ["Effective Software Testing"](https://ssciwr.github.io/effective-software-testing).

The project is a simple implementation of the game "tic-tac-toe" including a test suite.

Continuous integration is set up using [Github actions](https://github.com/ssciwr/effective-software-testing/actions/workflows/ci.yml) and [codecov](https://app.codecov.io/gh/ssciwr/effective-software-testing), which automatically run the tests and display a coverage report whenever a pull request is made.

## Getting started

To clone the repo and do an editable install of the package:

```
git clone https://github.com/ssciwr/effective-software-testing.git
cd effective-software-testing
python -m pip install --editable .[tests]
```

To run the tests:

```
python -m pytest
```

## Slides

[download slides as pdf](https://github.com/ssciwr/effective-software-testing/raw/main/docs/slides/slides.pdf) | [download course description as pdf](https://ssc.iwr.uni-heidelberg.de/sites/default/files/effective-software-testing.pdf)

## Acknowledgments

This repository was set up using the [SSC Cookiecutter for Python Packages](https://github.com/ssciwr/cookiecutter-python-package).
