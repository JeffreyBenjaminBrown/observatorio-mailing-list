#!/bin/bash

export PYTHONPATH=/mnt:/opt/conda/lib/python36.zip:/opt/conda/lib/python3.6:/opt/conda/lib/python3.6/lib-dynload:/opt/conda/lib/python3.6/site-packages
  # why that: # https://stackoverflow.com/questions/30378105/python-modules-not-found-over-terminal-but-on-python-shell-linux

cd /mnt/private/input && make downloads
cd /mnt && python3 src/main.py
