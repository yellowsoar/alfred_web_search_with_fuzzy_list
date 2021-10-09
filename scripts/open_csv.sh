#!/usr/bin/env bash

query=$1
filename=list.csv
custom_command=$(
    echo ${query} | sed -E "s@ .*@@"
)

if [ -x "${custom_command}" ]; then
    :
else
    custom_command=""
fi

if [ "${query}" == "reveal" ]; then
    open -R "${filename}"
elif [ "${query}" == "" ]; then
    open "${filename}"
else
    ${query} "${filename}"
fi
