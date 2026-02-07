#!/bin/bash
# install.sh - Dependency Installer for Aaayafuj_NSM.py

# Check for root privileges
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root (sudo ./install.sh)"
  exit
fi

echo "[*] Starting installation of Aaayafuj_NSM dependencies..."
echo "[*] Updating system repositories..."
apt-get update -y

echo "[*] Installing Nmap..."
apt-get install -y nmap

echo "[*] Installing SQLMap..."
apt-get install -y sqlmap

echo "[*] Installing Metasploit Framework..."
# Note: This might take time depending on your connection
apt-get install -y metasploit-framework

echo "[*] Installing core utilities (Curl, Python3, Pip)..."
apt-get install -y curl python3 python3-pip

echo "[*] Installing Python 'requests' library..."
pip3 install requests --break-system-packages 2>/dev/null || pip3 install requests

# Set permissions for the main tool
chmod +x Aaayafuj_NSM.py

echo "--------------------------------------------------------"
echo "[+] Installation complete!"
echo "[+] You can now run the tool using:"
echo "    python3 Aaayafuj_NSM.py --help"
echo "--------------------------------------------------------"
