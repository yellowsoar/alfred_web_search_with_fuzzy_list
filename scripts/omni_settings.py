#!/usr/bin/python

import os

env_var_default = [
    ["sfl_dir_csv", "csv"],
    ["sfl_dir_csv_icons", "csv_icons"],
    ["sfl_dir_icons", "icons"],
    ["sfl_dir_tmp", "tmp"],
    ["sfl_file_csv", "list.csv"],
]


def update_dict(dictionary, key, value):
    dictionary[key] = os.getenv(key, value)



env_var = {}

for _ in env_var_default:
    update_dict(env_var, _[0], _[1])
