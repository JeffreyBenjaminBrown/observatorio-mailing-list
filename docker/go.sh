#!/bin/bash

cd /mnt/private/input && make downloads
cd /mnt && python3 main.py
