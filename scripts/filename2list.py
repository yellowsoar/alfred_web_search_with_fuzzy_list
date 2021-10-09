#!/usr/bin/python

import os

DIR_CSV = os.getenv("sfl_dir_csv", "csv")
DIR_CSV_ICONS = os.getenv("sfl_dir_csv_icons", "csv_icons")

with open("tmp/list.csv", "w") as output_file:
    for _ in os.listdir(DIR_CSV):
        full_filename = os.path.splitext(_)
        if full_filename[1] == ".csv" and full_filename[0] not in (
            "list",
            "csvlist",
            # "tmp_list"
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
