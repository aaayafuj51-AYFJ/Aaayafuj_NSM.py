from utils import run_cmd, color_print, log_info

def run_msf(query):
    if not query:
        color_print("[!] Error: No search term provided.", "RED")
        return
    color_print(f"[*] Querying Metasploit database for: {query}", "BLUE")
    log_info(f"Metasploit query: {query}")
    run_cmd(["msfconsole", "-q", "-x", f"search {query}; exit"])
    input("\nTask finished. Press Enter to continue...")