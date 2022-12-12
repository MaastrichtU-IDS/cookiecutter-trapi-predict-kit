#!/usr/bin/env python

"""Code to run after generating the project."""

import os
import pathlib
import shutil

PROJECT_DIRECTORY = pathlib.Path(os.path.realpath(os.path.curdir)).resolve()
PACKAGE = PROJECT_DIRECTORY.joinpath("src", "{{ cookiecutter.module_name }}")
DOCS = PROJECT_DIRECTORY.joinpath("docs")
PACKAGE_NAME = "{{ cookiecutter.package_name }}"
MODEL_PATH = "src/" + "{{ cookiecutter.module_name }}"

RED = "\033[91m"
BOLD = "\033[1m"
END = "\033[0m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

if __name__ == '__main__':
    print(
        "✅ Your project has been successfully generated.\n"
        f"📂 Enter it with {BOLD}cd {PACKAGE_NAME}{END}\n"
        "✍️  To do:\n"
        f"- Check the citation generated in {BOLD}CITATION.cff{END} is correct\n"
        f"- Check the documentation in the {BOLD}README.md{END} to learn how to work with the code generated, and improve it at your convenience\n"
        f"- Add dependencies in {BOLD}pyproject.toml{END}\n"
        f"- Add your code for training and predictions in {BOLD}{MODEL_PATH}/{END}"
    )