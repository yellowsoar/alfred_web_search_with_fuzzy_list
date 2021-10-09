#!/usr/bin/python

import os

for _ in ['tmp']:
    if not os.path.isdir("tmp"):
        os.mkdir("tmp")
