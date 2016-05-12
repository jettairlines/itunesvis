#!/bin/bash
if [ ! -f /iTunes Music Library.xml ]; then
    echo "File not found!"
    exit 1;
fi

data="python data.py"
server="python -m SimpleHTTPServer"

eval $data
eval $server
echo "Now nevagate to localhost:8000..."