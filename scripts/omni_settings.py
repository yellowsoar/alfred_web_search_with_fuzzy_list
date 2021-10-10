#!/usr/bin/python

import os


def update_dict(dictinary, key, value):
    dictinary[key] = os.getenv(key, value)


env_var = {}
for _ in [
    ["sfl_dir_csv", "csv"],
    ["sfl_dir_csv_icons", "csv_icons"],
    ["sfl_dir_icons", "icons"],
    ["sfl_dir_tmp", "tmp"],
    ["sfl_file_csv", "list.csv"],
]:
    update_dict(env_var, _[0], _[1])
