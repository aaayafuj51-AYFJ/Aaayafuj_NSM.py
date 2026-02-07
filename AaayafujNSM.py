#!/usr/bin/env python3
"""
AaayafujNSM CLI Suite
Main entry point for the modular security toolkit.
"""
import sys
import os

# Add the current directory to sys.path to ensure modular imports work
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from menu import main_menu
    from utils import setup_logging, color_print
except ImportError as e:
    print(f"[!] Critical Import Error: {e}")
    print("[*] Please ensure all module files (menu.py, utils.py, etc.) are in the same directory.")
    sys.exit(1)

def main():
    setup_logging()
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\n\033[93m[!] Session interrupted by user. Exiting...\033[0m")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n\033[91m[!] A critical error occurred: {e}\033[0m")
        sys.exit(1)

if __name__ == "__main__":
    main()
