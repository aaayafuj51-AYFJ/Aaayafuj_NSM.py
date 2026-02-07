#!/bin/bash
# Aaayafuj_NSM.sh - Launcher

# ANSI Colors
RED='\033[0;31m'
NC='\033[0m'

# Check for Python 3
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}[!] Error: Python 3 is required but not installed.${NC}"
    exit 1
fi

# Get absolute path to script directory
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Execute the main Python script
python3 "$DIR/Aaayafuj_NSM.py" "$@"
