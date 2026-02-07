
import React from 'react';

export const BANNER_TEXT = `
 █████╗  █████╗  █████╗ ██╗   ██╗███████╗██╗   ██╗     ███╗   ██╗███████╗███╗   ███╗
██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝██║   ██║     ████╗  ██║██╔════╝████╗ ████║
███████║███████║███████║ ╚████╔╝ █████╗  ██║   ██║     ██╔██╗ ██║███████╗██╔████╔██║
██╔══██║██╔══██║██╔══██║  ╚██╔╝  ██╔══╝  ██║   ██║     ██║╚██╗██║╚════██║██║╚██╔╝██║
██║  ██║██║  ██║██║  ██║   ██║   ██║     ╚██████╔╝     ██║ ╚████║███████║██║ ╚═╝ ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝      ╚═════╝      ╚═╝  ╚═══╝╚══════╝╚═╝     ╚═╝
                                v1.0.0 - Advanced Security Suite
`;

export const PYTHON_TOOL_CONTENT = `
#!/usr/bin/env python3
# Aaayafuj_NSM.py - Built by Python Script
# A CLI implementation of the Advanced Network Security Manager

import os
import sys
import argparse
import subprocess

def banner():
    print("""
    Aaayafuj_NSM.py
    ---------------------------------
    1. Nmap Scanning
    2. SQLMap Testing
    3. Metasploit Search
    4. DNS Lookup
    5. Info Gathering
    ---------------------------------
    """)

def run_command(cmd_list):
    try:
        result = subprocess.run(cmd_list, capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"Error executing command: {e}")

def main():
    parser = argparse.ArgumentParser(description="Aaayafuj_NSM.py - Security Suite")
    parser.add_argument("--nmap", help="Run nmap on target")
    parser.add_argument("--sqlmap", help="Run sqlmap on URL")
    parser.add_argument("--msf", help="Search Metasploit modules")
    parser.add_argument("--lookup", help="Perform DNS/WHOIS lookup")
    parser.add_argument("--gather", help="Gather info on IP/URL")

    if len(sys.argv) == 1:
        banner()
        parser.print_help()
        return

    args = parser.parse_args()

    if args.nmap:
        print(f"[*] Starting Nmap scan on {args.nmap}...")
        run_command(["nmap", "-A", "-T4", args.nmap])
    
    if args.sqlmap:
        print(f"[*] Testing {args.sqlmap} for SQL injection...")
        run_command(["sqlmap", "-u", args.sqlmap, "--batch", "--banner"])

    if args.msf:
        print(f"[*] Searching Metasploit for {args.msf}...")
        run_command(["msfconsole", "-x", f"search {args.msf}; exit"])

    if args.lookup:
        print(f"[*] Performing WHOIS lookup on {args.lookup}...")
        run_command(["whois", args.lookup])

    if args.gather:
        print(f"[*] Gathering OSINT for {args.gather}...")
        run_command(["curl", f"https://ipinfo.io/{args.gather}/json"])

if __name__ == "__main__":
    main()
`;

export const SH_INSTALLER_CONTENT = `
#!/bin/bash
# install.sh for Aaayafuj_NSM.py

echo "Installing dependencies for Aaayafuj_NSM.py..."
sudo apt update
sudo apt install -y nmap sqlmap metasploit-framework curl python3 python3-pip

chmod +x Aaayafuj_NSM.py
echo "Setup complete. Run with: ./Aaayafuj_NSM.py --help"
`;
