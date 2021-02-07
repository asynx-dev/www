#!/usr/bin/python3

# Cleans after jobs

import os
import subprocess
import shutil

def clean():
    except_flag = 0

    try:
        shutil.rmtree(os.path.join(os.path.dirname(__file__), 'vendor'))
    except:
        print("WARNING: Can't remove vendor (gem location) directory")
        except_flag = 1

    try:
        shutil.rmtree(os.path.join(os.path.dirname(__file__), '_site'))
    except:
        print("WARNING: Can't remove _site (Jekyll output) directory")
        except_flag = 1

    try:
        subprocess.run([shutil.which('pipenv'), "--rm"])
    except:
        print("WARNING: Can't remove pipenv virtualenv from the system")
        except_flag = 1

    if (except_flag):
        raise Exception("Some steps didn't finish correctly.")

if __name__ == '__main__':
    try:
        clean()
    except:
        print("Some steps didn't finish correctly.")

