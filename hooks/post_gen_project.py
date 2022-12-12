#!/usr/bin/env python

"""Code to run after generating the project."""

import os
import pathlib
import shutil

PROJECT_DIRECTORY = pathlib.Path(os.path.realpath(os.path.curdir)).resolve()
PACKAGE = PROJECT_DIRECTORY.joinpath("src", "{{ cookiecutter.module_name }}")
DOCS = PROJECT_DIRECTORY.joinpath("docs")
