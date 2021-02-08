#!/usr/bin/python3

# Some helper functions

import os
import subprocess
from subprocess import PIPE
import datetime
import argparse
import shutil

parser = argparse.ArgumentParser(description='Function',
                                formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument('fn',
                    choices=['build-info'],
                    help='''
                    build-info: Populate build.info.txt
                        ''')

args = parser.parse_args()

if args.fn == "build-info":
    with open(os.path.join(os.path.dirname(__file__), '_site', 'build.info.txt'), 'w') as f:
        f.write(subprocess.run([shutil.which('bundle'), "list"], stdout=PIPE, stderr=PIPE).stdout.decode())
        f.write(subprocess.run([shutil.which('bundle'), "exec", "jekyll", "--version"], stdout=PIPE, stderr=PIPE).stdout.decode())
        f.write(subprocess.run([shutil.which('git'), "log", "-1", "--oneline"], stdout=PIPE, stderr=PIPE).stdout.decode())
        f.write(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")+' UTC\n')
