#!/usr/bin/python
# Script to set up basic Django structure

import urllib
import re
import time
import pdb

def main():

    uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
    nothing_rep = "and the next nothing is (\d+)"
    nothing = "12345" # You'll later be asked to change this
                      # to "46059" and re-run the script.
    pdb.set_trace()

    while True:
        try:
            source = urllib.urlopen(uri % nothing).read()
            nothing = re.search(nothing_rep, source).group(1)
        except:
            break

    print (nothing)

if __name__ == '__main__':
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
