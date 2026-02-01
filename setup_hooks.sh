#!/bin/bash
# Install pre-commit if not installed
if ! command -v pre-commit &> /dev/null
then
    echo "pre-commit not found. Installing..."
    pip install pre-commit
fi

# Install hooks
pre-commit install
echo "Pre-commit hooks installed successfully."
