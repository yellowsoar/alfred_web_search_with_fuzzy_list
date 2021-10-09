#!/usr/bin/python

import os
import shutil
import sys

query = os.getenv('query', '')
shutil.copyfile("csv/" + query, "tmp/list.csv")
query = ""

sys.stdout.write(query)
