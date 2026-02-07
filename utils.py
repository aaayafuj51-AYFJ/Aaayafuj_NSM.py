import os
import subprocess
import logging

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
    banner = r"""
     /.\                                        .|';                    '||\   ||` .|'''|  '||\   /||` 
    // \\                                       ||               ''      ||\\  ||  ||       ||\\.//||  
   //...\\     '''|.   '''|.  '||  ||`  '''|.  '||'  '||  ||`    || ---  || \\ ||  `|'''|,  ||     ||  
  //     \\   .|''||  .|''||   `|..||  .|''||   ||    ||  ||     ||      ||  \\||   .   ||  ||     ||  
.//       \\. `|..||. `|..||.      ||  `|..||. .||.   `|..'|.    ||     .||   \||.  |...|' .||     ||. 
                                ,  |'                            ||                                    
                                 ''                           `..|'                                  
    """
    print("\033[1;32m" + banner + "\033[0m")
    print("\033[1;36m" + "           ADVANCED NETWORK SECURITY MANAGER (CLI)" + "\033[0m\n")

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

def run_cmd(cmd):
    try:
        if isinstance(cmd, list):
            subprocess.run(cmd, check=False)
        else:
            subprocess.run(cmd, shell=True, check=False)
    except FileNotFoundError:
        color_print("[!] Error: Tool not found. Please install dependencies.", "RED")
    except Exception as e:
        color_print(f"[!] Execution error: {e}", "RED")
