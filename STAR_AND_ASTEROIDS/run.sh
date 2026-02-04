#!/bin/bash
python3 create.py
# Run SWIFT
../../../swift --self-gravity --threads=4 config.yml 2>&1 | tee output.log
