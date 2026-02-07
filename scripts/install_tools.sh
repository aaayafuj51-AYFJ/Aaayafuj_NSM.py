#!/bin/bash
# install_tools.sh - Dependency Setup

if [ "$EUID" -ne 0 ]; then
  echo -e "\e[91m[-] Please run as root: sudo bash scripts/install_tools.sh\e[0m"
  exit 1
fi

echo -e "\e[92m[*] Setting up Aaayafuj_NSM Suite...\e[0m"

# Install System Tools
apt update -y
apt install -y nmap sqlmap metasploit-framework whois curl git \
               python3-pip python3-dev build-essential libssl-dev libffi-dev

# Fix Python Environment (Prevents Rust/Compilation Errors)
echo -e "\e[94m[*] Optimizing Python environment...\e[0m"
python3 -m pip install --upgrade pip setuptools wheel --break-system-packages 2>/dev/null || \
python3 -m pip install --upgrade pip setuptools wheel

# Install Requirements
python3 -m pip install requests --break-system-packages 2>/dev/null || \
python3 -m pip install requests

# Permissions
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASE="$(dirname "$DIR")"
chmod +x "$BASE/Aaayafuj_NSM.py"
chmod +x "$BASE/Aaayafuj_NSM.sh"

echo -e "\e[92m[+] Setup complete. Start tool with: ./Aaayafuj_NSM.sh\e[0m"
