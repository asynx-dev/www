#!/usr/bin/python3

# This file is used to run test server on localhost while working on the site
# Please check README.md for proper flow for development

import subprocess
import shutil

subprocess.run([shutil.which('bundle'), "exec", "jekyll", "serve", "--config", "_config.yml", "--watch", "--livereload"])
