#!/usr/bin/env bash

export PATH="/usr/local/bin:${PATH}"
query=$1
custom_command=$(
    echo ${query} | sed -E "s@ .*@@"
)

if [ -x "${custom_command}" ]; then
    :
else
    custom_command=""
fi

if [ "${query}" == "reveal" ]; then
    open -R "${sfl_file_csv}"
elif [ "${query}" == "" ]; then
    open "${sfl_file_csv}"
else
    ${query} "${sfl_file_csv}"
fi
