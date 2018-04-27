#!/bin/bash

cd /mnt/private && make downloads
cd /mnt && python3 main.py
