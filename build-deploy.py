#!/usr/bin/python3

# This script build the site for publishing.

import os
from pathlib import Path
from shutil import copyfile
import subprocess
import datetime

subprocess.run(["pipenv", "install"])
subprocess.run(["pipenv", "run", "mkdocs", "build", "--clean", "--config-file", "mkdocs-deploy.yml"])

Path(os.path.join(os.path.dirname(__file__), 'site', '.nojekyll')).touch()
copyfile(os.path.join(os.path.dirname(__file__), 'CNAME'), os.path.join(os.path.dirname(__file__), 'site', 'CNAME'))

with open(os.path.join(os.path.dirname(__file__), 'site', 'build.info.txt'), 'a') as f:
    f.write(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")+' UTC\n')
    f.write(subprocess.run(["pipenv", "run", "mkdocs", "--version"], capture_output=True, text=True).stdout)
    f.write(subprocess.run(["git", "log", "-1", "--oneline"], capture_output=True, text=True).stdout)

#subprocess.run(["pipenv", "--rm"])