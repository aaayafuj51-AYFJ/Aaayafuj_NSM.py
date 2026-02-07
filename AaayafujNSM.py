#!/usr/bin/env python3
import os
import sys

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    target = os.path.join(current_dir, "Aaayafuj_NSM.py")
    if os.path.exists(target):
        os.execv(sys.executable, [sys.executable, target] + sys.argv[1:])
    else:
        print("[!] Aaayafuj_NSM.py not found.")
