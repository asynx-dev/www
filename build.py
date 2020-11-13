#!/usr/bin/python3

# this file is used to build the site with localhost
# configuration. Not suitable for development phase since this will install
# and destroy the virtual environment.
# Please check README.md for proper flow for development

import subprocess

subprocess.run(["pipenv", "install"])
subprocess.run(["pipenv", "run", "mkdocs", "build", "--clean", "--verbose", "--config-file", "mkdocs.yml"])
#subprocess.run(["pipenv", "--rm"])
