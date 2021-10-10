#!/usr/bin/python

import os
import shutil
import sys

import omni_settings

env_var = omni_settings.env_var

query = os.getenv('query', '')
path_csv_query = "/".join(
    [
        env_var["sfl_dir_csv"],
        query,
    ]
)
path_csv_tmp = "/".join(
    [
        env_var["sfl_dir_tmp"],
        env_var["sfl_file_csv"],
    ]
)

shutil.copyfile(path_csv_query, path_csv_tmp)
sys.stdout.write("")
