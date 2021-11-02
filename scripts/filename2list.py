#!/usr/bin/python

import os

from omni_settings import env_var, sfl_var

with open(
    os.path.join(env_var['sfl_dir_tmp'], "list.csv"), "w"
) as output_file:
    for _ in os.listdir(env_var['sfl_dir_csv']):
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
                        env_var['sfl_dir_csv_icons']
                        + "/"
                        + full_filename[0]
                        + ".png",
                    ]
                )
                + "\n"
            )
