import requests
import json
from utils import color_print, log_info

def run_gather(target):
    if not target:
        color_print("[!] Error: No target provided.", "RED")
        return
        
    color_print(f"[*] Gathering intelligence for: {target}", "BLUE")
    log_info(f"OSINT gathering: {target}")
    
    try:
        response = requests.get(f"http://ip-api.com/json/{target}")
        data = response.json()
        
        if data.get('status') == 'success':
            color_print("\n[+] OSINT Report Summary:", "GREEN")
            for key, val in data.items():
                print(f"    {key.capitalize():<15}: {val}")
        else:
            color_print(f"[!] OSINT API Error: {data.get('message', 'Target unreachable')}", "RED")
            
    except Exception as e:
        color_print(f"[!] OSINT Connectivity issue: {e}", "RED")
        
    input("\nTask finished. Press Enter to continue...")