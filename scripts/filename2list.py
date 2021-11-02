#!/usr/bin/python

import os

import omni_settings

env_var = omni_settings.env_var

DIR_CSV = env_var['sfl_dir_csv']
DIR_CSV_ICONS = env_var['sfl_dir_csv_icons']
DIR_TMP = env_var['sfl_dir_tmp']
FILE_CSV = env_var['sfl_file_csv']

with open(os.path.join(DIR_TMP, "list.csv"), "w") as output_file:
    for _ in os.listdir(DIR_CSV):
        full_filename = os.path.splitext(_)
        if (
            full_filename[1] == ".csv"
            and full_filename[0] not in env_var['sfl_file_csv_ignore']
        ):
            output_file.write(
                ",".join(
                    [
                        full_filename[0],
                        "",
                        full_filename[0] + full_filename[1],
                        DIR_CSV_ICONS + "/" + full_filename[0] + ".png",
                    ]
                )
                + "\n"
            )
