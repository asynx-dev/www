# This test search a valid GA code at the output.
# Just for simplicity, search the GA code in one file. Of course, it is better
# check all HTML files.

import os

def check_GA(relfile, code):

    dirname = os.path.dirname(__file__)
    file = os.path.join(dirname, relfile)

    if os.path.exists(file):
        with open(file, 'r') as f:
            try:
                return (code in f.read())
            except :
                raise Exception("Couldn't read file for GA test")
    else:
        print("File doesn't exist")
        return False

def test_answer():
    assert check_GA('../_site/index.html','UA-180670653-1') == True
