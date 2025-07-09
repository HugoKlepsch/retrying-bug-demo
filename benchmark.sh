#!/bin/bash

echo "=== Retrying Library Benchmark Comparison ==="
echo

echo "--- Testing with retrying 1.3.4 ---"
. .venv-1.3.4/bin/activate
python retrying_bug_demo.py
deactivate
echo

# Benchmark with retrying 1.3.6
echo "--- Testing with retrying 1.3.6 ---"
. .venv-1.3.6/bin/activate
python retrying_bug_demo.py
deactivate
