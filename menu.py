from utils import clear_screen, get_input, color_print
from nmap_tool import run_nmap
from sqlmap_tool import run_sqlmap
from metasploit_tool import run_msf
from lookup import run_lookup
from gather import run_gather

def main_menu():
    while True:
        print("\033[1;37m" + "--- MAIN MODULES ---" + "\033[0m")
        print(" [1] Nmap (Scan)")
        print(" [2] SQLMap (Inject)")
        print(" [3] Metasploit (Search)")
        print(" [4] Lookup (DNS/WHOIS)")
        print(" [5] Gathering (OSINT)")
        print(" [0] Exit")
        
        choice = get_input("Main")
        
        if choice == '1':
            target = get_input("Target")
            run_nmap(target)
        elif choice == '2':
            url = get_input("Target URL")
            run_sqlmap(url)
        elif choice == '3':
            query = get_input("Search Term")
            run_msf(query)
        elif choice == '4':
            domain = get_input("Domain")
            run_lookup(domain)
        elif choice == '5':
            target = get_input("Target")
            run_gather(target)
        elif choice == '0':
            color_print("Terminating...", "YELLOW")
            break
        else:
            color_print("Invalid choice.", "RED")
