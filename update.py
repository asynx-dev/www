#!/usr/bin/python3

# This file is used to update necessary dependencies and environment to latest
# version. It can be also used to install the environment if it is missing.

import subprocess
import shutil

def update():
    try:
        subprocess.run([shutil.which('bundle'), "update"])
        subprocess.run([shutil.which('pipenv'), "update"])
    except:
        raise

if __name__ == '__main__':
    try:
        update()
    except:
        raise
