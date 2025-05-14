#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Activate virtual environment
source venv/Scripts/activate

# Run pytest
echo "Running test suite with pytest..."
pytest test_app.py

# Capture exit code from pytest
EXIT_CODE=$?

# Exit with success (0) if tests pass, otherwise with failure (1)
if [ $EXIT_CODE -eq 0 ]; then
    echo "All tests passed successfully."
    exit 0
else
    echo "Some tests failed."
    exit 1
fi
