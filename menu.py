import os
from utils import print_banner, clear_screen, get_input, color_print
from nmap_tool import run_nmap
from sqlmap_tool import run_sqlmap
from metasploit_tool import run_msf
from lookup import run_lookup
from gather import run_gather

def main_menu():
    while True:
        clear_screen()
        print_banner()
        print(" [1] Nmap - Network Security Scan")
        print(" [2] SQLMap - Web Vulnerability Analysis")
        print(" [3] Metasploit - Exploit Module Search")
        print(" [4] Lookup - DNS & WHOIS Information")
        print(" [5] Gathering - OSINT Intelligence")
        print(" [0] Exit Application")
        print("-" * 50)
        
        choice = get_input("Choice")
        
        if choice == '1':
            target = get_input("Target IP/Domain")
            run_nmap(target)
        elif choice == '2':
            url = get_input("Target URL")
            run_sqlmap(url)
        elif choice == '3':
            query = get_input("Search Term")
            run_msf(query)
        elif choice == '4':
            domain = get_input("Domain Name")
            run_lookup(domain)
        elif choice == '5':
            target = get_input("Target (IP/Domain)")
            run_gather(target)
        elif choice == '0':
            color_print("[*] Terminating session...", "YELLOW")
            break
        else:
            color_print("[!] Invalid input detected.", "RED")
            input("\nPress Enter to try again...")