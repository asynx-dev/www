#!/usr/bin/python3

# This file is used to build the site with localconfiguration.
# Please check README.md for proper flow for development

import subprocess
import shutil

subprocess.run([shutil.which('bundle'), "exec", "jekyll", "build", "--config", "_config.yml", "--verbose"])
