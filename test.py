#!/usr/bin/python3

# This script runs tests

import subprocess
import argparse

parser = argparse.ArgumentParser(description='Run tests',
                                formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument('test',
                    default='pytest',
                    choices=['all','pytest','markdownlint'],
                    nargs='?',
                    help='''
                    all: Runs both pytest and markdownlint tests
                    pytest: Runs pytest based tests. This will run all test except markdownlint
                    markdownlint: Run linter for markdown files using. markdownlint-cli from npm should be installed.
                    (default: %(default)s)
                        ''')

args = parser.parse_args()

if args.test == "all" or args.test == "pytest":
    print("Running pytest...")
    subprocess.run(["pipenv", "run", "pytest", "-q", "test/test_ga.py"], check=True)
    print("Done with pytest")

if args.test == "all" or args.test == "markdownlint":
    print("Running markdownlint...")
    subprocess.run(["markdownlint", "./"], shell=True, check=True)
    subprocess.run(["markdownlint", "docs"], shell=True, check=True)
    print("Done with markdownlint")

print("All finished")
