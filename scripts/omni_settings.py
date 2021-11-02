#!/usr/bin/python

import os

env_var_default = [
    ["sfl_dir_csv", "demo/csv"],
    ["sfl_dir_csv_icons", "demo/csv_icons"],
    ["sfl_dir_icons", "demo/icons"],
    ["sfl_dir_tmp", "tmp"],
    ["sfl_file_csv", "demo/list.csv"],
    ["sfl_file_csv_ignore", []],
]
env_var_list_default = ""
env_var_list_delimiter = ","
sfl_var = {
    "dir_work_csv": "csv",
    "dir_work_csv_icons": "icons",
    "file_work_csv": "list.csv",
    "file_work_csv_icons": "icons",
}


def update_dict(dictionary, key, value):
    dictionary[key] = os.getenv(key, value)
    if isinstance(value, str):
        dictionary[key] = os.getenv(key, value)
    elif isinstance(value, list):
        env_var_list_current = os.getenv(key, env_var_list_default)

        if env_var_list_current != env_var_list_default:
            dictionary[key] = env_var_list_current.split(
                env_var_list_delimiter
            )
        else:
            dictionary[key] = value


env_var = {}

for _ in env_var_default:
    update_dict(env_var, _[0], _[1])
