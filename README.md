# OneDep Core Testing Library

[![Build Status](https://dev.azure.com/wwPDB/wwPDB%20Python%20Projects/_apis/build/status/wwPDB.py-wwpdb_utils_testing?branchName=master)](https://dev.azure.com/wwPDB/wwPDB%20Python%20Projects/_build/latest?definitionId=1&branchName=master)

## Introduction

This repository can be used by the test suite to setup/test for running environments

The code in here will allow for common setup of site-config harness as
well of allowing for fixtures to test the environment to determine if
a test can be invoked.

### Installation

Download the library source software from the project repository:

```bash

git clone  --recurse-submodules  https://github.com/wwPDB/py-wwpdb_utils_testing.git

```

Optionally, run test suite using the Tox test runner.

```bash
tox
```

Installation is via the program [pip](https://pypi.python.org/pypi/pip).

```bash
pip install wwpdb.utils.testing

or from the local repository:

pip install .
```

