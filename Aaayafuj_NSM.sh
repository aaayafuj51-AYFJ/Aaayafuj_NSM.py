#!/bin/bash
# Aaayafuj_NSM.sh - Bash Launcher

# Check for Python 3
if ! command -v python3 &> /dev/null
then
    echo -e "\e[91m[!] Error: Python 3 is not installed.\e[0m"
    exit 1
fi

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Run the main Python tool
python3 "$SCRIPT_DIR/Aaayafuj_NSM.py" "$@"
