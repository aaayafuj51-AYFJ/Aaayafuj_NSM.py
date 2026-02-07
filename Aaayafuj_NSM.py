#!/usr/bin/env python3
"""
Aaayafuj_NSM.py - Advanced Network Security Manager
Primary entry point for the security toolset.
"""
import sys
import os

# Ensure script directory is in path for modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from utils import print_banner, setup_logging, color_print
    from menu import main_menu
except ImportError as e:
    print(f"\033[91m[!] Dependency Error: {e}\033[0m")
    print("[*] Run: sudo bash scripts/install_tools.sh to fix dependencies.")
    sys.exit(1)

def main():
    # Initialize environment
    setup_logging()
    
    # Display the requested banner
    print_banner()
    
    try:
        # Launch main interactive menu
        main_menu()
    except KeyboardInterrupt:
        print("\n\n\033[93m[!] Session terminated by user.\033[0m")
        sys.exit(0)
    except Exception as e:
        color_print(f"\n[!] A fatal error occurred: {e}", "RED")
        sys.exit(1)

if __name__ == "__main__":
    main()
