import sys
import os
from menu import main_menu
from utils import setup_logging

def main():
    # Ensure current directory is in search path for modular imports
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    
    setup_logging()
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n[!] Shutdown requested by user. Goodbye.")
        sys.exit(0)
    except Exception as e:
        print(f"\n[!] Critical System Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()