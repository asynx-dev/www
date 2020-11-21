#!/usr/bin/python3

# This script build the site for scheduled checks which are not intended to
# deploy

import subprocess

subprocess.run(["pipenv", "install"])
subprocess.run(["pipenv", "run", "mkdocs", "build", "--clean", "--strict", "--verbose", "--config-file", "mkdocs-cron.yml"], check=True)
