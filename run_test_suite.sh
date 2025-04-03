#!/usr/bin/env bash

# Script Name: run_test_suite.sh
# Description: Runs tests in virtual environment. Returns 0 if all tests pass, otherwise 1.
# Author: Jaleel Abdur-Raheem
# Date: 2025-04-03
# Usage: ./run_test_suite.sh
# Notes: 

source "$(dirname "$0")/venv/bin/activate"

pytest --maxfail=1 > /dev/null 2>&1

EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
  echo "All tests passed!"
  exit 0
else
  echo "Some tests failed!"
  exit 1
fi