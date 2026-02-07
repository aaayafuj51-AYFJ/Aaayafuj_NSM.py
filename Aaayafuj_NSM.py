#!/usr/bin/env python3
# Wrapper for AaayafujNSM.py
import os
import sys

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    target_script = os.path.join(current_dir, "AaayafujNSM.py")
    
    if os.path.exists(target_script):
        os.execv(sys.executable, [sys.executable, target_script] + sys.argv[1:])
    else:
        print("[!] AaayafujNSM.py not found in the current directory.")
