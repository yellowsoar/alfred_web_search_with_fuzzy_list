#!/usr/bin/python

import os

import omni_settings

env_var = omni_settings.env_var
sfl_var = omni_settings.sfl_var

dir_check_list = [
    env_var['sfl_dir_tmp'],
]
dir_symbolic_list = [
    [env_var['sfl_dir_csv'], sfl_var['dir_work_csv']],
    [env_var['sfl_dir_csv_icons'], sfl_var['dir_work_csv_icons']],
    [env_var['sfl_file_csv'], sfl_var['file_work_csv']],
]


for _ in dir_check_list:
    if not os.path.isdir(_):
        os.mkdir(_)

for _ in dir_symbolic_list:
    dir_symbolic_target = _[1]
    dir_symbolic_source = os.path.abspath(_[0])
    if any(
        [
            os.path.isdir(dir_symbolic_target),
            os.path.islink(dir_symbolic_target),
        ]
    ):
        os.remove(dir_symbolic_target)
    os.symlink(dir_symbolic_source, dir_symbolic_target)
