#!/usr/bin/python

import os

import omni_settings

env_var = omni_settings.env_var
dir_temp = env_var['sfl_dir_tmp']
dir_check_list = [dir_temp]

for _ in dir_check_list:
    if not os.path.isdir(dir_temp):
        os.mkdir(dir_temp)
