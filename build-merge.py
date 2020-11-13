#!/usr/bin/python3

# This script build the site for merge request checking

import subprocess

subprocess.run(["pipenv", "install"])
subprocess.run(["pipenv", "run", "mkdocs", "build", "--clean", "--strict", "--verbose", "--config-file", "mkdocs-merge.yml"])
