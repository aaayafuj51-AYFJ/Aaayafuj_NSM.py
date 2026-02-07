#!/bin/bash
# AaayafujNSM Dependency Installer
# Optimized for local and GitHub cloned installations

if [ "$EUID" -ne 0 ]; then
  echo "[-] Please run as root (sudo bash scripts/install_tools.sh)"
  exit
fi

echo "[*] Starting AaayafujNSM environment setup..."

# Check if we are in a git repository
if [ -d ".git" ]; then
    echo "[+] Detected GitHub repository context."
fi

echo "[*] Updating system and installing toolset..."
apt update -y
apt install -y nmap sqlmap metasploit-framework whois curl python3-pip git

echo "[*] Installing Python dependencies..."
pip3 install requests --break-system-packages 2>/dev/null || pip3 install requests

# Get the script's directory to set correct permissions
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASE_DIR="$(dirname "$SCRIPT_DIR")"

echo "[*] Setting execution permissions in $BASE_DIR..."
chmod +x "$BASE_DIR/AaayafujNSM.py" 2>/dev/null
chmod +x "$BASE_DIR/Aaayafuj_NSM.py" 2>/dev/null
chmod +x "$BASE_DIR/main.py" 2>/dev/null

echo "--------------------------------------------------------"
echo "[+] Installation successful."
echo "[*] System: $(uname -a)"
echo "[*] Entry Point: python3 AaayafujNSM.py"
echo "--------------------------------------------------------"
