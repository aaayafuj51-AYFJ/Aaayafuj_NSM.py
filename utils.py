import os
import subprocess
import logging
from datetime import datetime

def setup_logging():
    if not os.path.exists('logs'):
        try: os.makedirs('logs')
        except: pass
            
    logging.basicConfig(
        filename='logs/app.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    # New requested ASCII art banner
    banner = r"""
     /.\                                        .|';                    '||\   ||` .|'''|  '||\   /||` 
    // \\                                       ||               ''      ||\\  ||  ||       ||\\.//||  
   //...\\     '''|.   '''|.  '||  ||`  '''|.  '||'  '||  ||`    || ---  || \\ ||  `|'''|,  ||     ||  
  //     \\   .|''||  .|''||   `|..||  .|''||   ||    ||  ||     ||      ||  \\||   .   ||  ||     ||  
.//       \\. `|..||. `|..||.      ||  `|..||. .||.   `|..'|.    ||     .||   \||.  |...|' .||     ||. 
                                ,  |'                            ||                                    
                                 ''                           `..|'                                  
           ADVANCED NETWORK SECURITY MANAGER (CLI)
    """
    # Using a green "gd" color style (Green Default/Bold)
    print("\033[1;32m" + banner + "\033[0m")

def get_input(prompt):
    return input(f"\033[94m[Aaayafuj@{prompt}]\033[0m $ ").strip()

def color_print(text, color="GREEN"):
    colors = {
        "RED": "\033[91m",
        "GREEN": "\033[92m",
        "YELLOW": "\033[93m",
        "BLUE": "\033[94m",
        "CYAN": "\033[96m",
        "END": "\033[0m"
    }
    print(f"{colors.get(color, '')}{text}{colors['END']}")

def log_info(msg):
    logging.info(msg)

def run_cmd(cmd):
    try:
        # If cmd is a list, join it for display, else it's a string
        cmd_str = " ".join(cmd) if isinstance(cmd, list) else cmd
        color_print(f"[*] Executing: {cmd_str}", "CYAN")
        subprocess.run(cmd, shell=isinstance(cmd, str), check=False)
    except FileNotFoundError:
        color_print(f"[!] Error: Binary '{cmd[0] if isinstance(cmd, list) else cmd}' is missing. Run installer.", "RED")
    except Exception as e:
        color_print(f"[!] Execution error: {e}", "RED")
