import os

with open("tmp/list.csv", "w") as output_file:
    for _ in os.listdir("csv"):
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
                        "csv_icons/" + full_filename[0] + ".png",
                    ]
                )
                + "\n"
            )
            # print(full_filename[0] + full_filename[1])
