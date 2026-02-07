#!/bin/bash
# AaayafujNSM Robust Dependency Installer
# Optimized for Linux (Debian/Kali/Ubuntu)

if [ "$EUID" -ne 0 ]; then
  echo -e "\e[91m[-] Please run as root: sudo bash scripts/install_tools.sh\e[0m"
  exit 1
fi

echo -e "\e[92m[*] Initializing AaayafujNSM Environment Setup...\e[0m"

# 1. Install System Dependencies & Build Tools
echo -e "\e[94m[*] Installing system binaries and build essentials...\e[0m"
apt update -y
apt install -y nmap sqlmap metasploit-framework whois curl git \
               python3-pip python3-dev build-essential libssl-dev libffi-dev

# 2. Upgrade Pip, Setuptools, and Wheel
# This is crucial to avoid "Rust toolchain" errors by ensuring binary wheels are prioritized
echo -e "\e[94m[*] Upgrading Python package managers...\e[0m"
python3 -m pip install --upgrade pip setuptools wheel --break-system-packages 2>/dev/null || \
python3 -m pip install --upgrade pip setuptools wheel

# 3. Install Python Requirements
echo -e "\e[94m[*] Installing application dependencies...\e[0m"
if [ -f "requirements.txt" ]; then
    python3 -m pip install -r requirements.txt --break-system-packages 2>/dev/null || \
    python3 -m pip install -r requirements.txt
else
    python3 -m pip install requests --break-system-packages 2>/dev/null || \
    python3 -m pip install requests
fi

# 4. Finalize Permissions
BASE_DIR="$(dirname "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd )")"
echo -e "\e[94m[*] Finalizing permissions in $BASE_DIR...\e[0m"
chmod +x "$BASE_DIR/AaayafujNSM.py" 2>/dev/null
chmod +x "$BASE_DIR/Aaayafuj_NSM.py" 2>/dev/null
chmod +x "$BASE_DIR/main.py" 2>/dev/null

echo -e "\e[92m"
echo "--------------------------------------------------------"
echo "[+] Installation Successful!"
echo "[*] Launch with: python3 AaayafujNSM.py"
echo "--------------------------------------------------------"
echo -e "\e[0m"
