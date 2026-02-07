import socket
from utils import color_print, log_info, run_cmd

def run_lookup(domain):
    if not domain:
        color_print("[!] Error: No domain provided.", "RED")
        return
    
    color_print(f"[*] Resolving DNS for: {domain}", "BLUE")
    log_info(f"DNS lookup: {domain}")
    
    try:
        ip = socket.gethostbyname(domain)
        color_print(f"[+] IP Resolved: {ip}", "GREEN")
        
        color_print("\n[*] Fetching WHOIS data...", "BLUE")
        run_cmd(["whois", domain])
    except Exception as e:
        color_print(f"[!] Lookup failure: {e}", "RED")
        
    input("\nTask finished. Press Enter to continue...")