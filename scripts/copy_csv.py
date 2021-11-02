#!/usr/bin/python

import os
import shutil
import sys

from omni_settings import env_var, sfl_var

query = os.getenv('query', '')
path_csv_query = os.path.join(sfl_var['dir_work_csv'], query)
path_csv_tmp = os.path.join(env_var["sfl_dir_tmp"], sfl_var['file_work_csv'])

shutil.copyfile(path_csv_query, path_csv_tmp)
sys.stdout.write("")
