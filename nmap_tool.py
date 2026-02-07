from utils import run_cmd, color_print, log_info, get_input, clear_screen

NMAP_PRESETS = [
    "nmap {target}",
    "nmap -A {target}",
    "nmap -sS {target}",
    "nmap -sT {target}",
    "nmap -sU {target}",
    "nmap -sA {target}",
    "nmap -sW {target}",
    "nmap -sM {target}",
    "nmap -sN {target}",
    "nmap -sF {target}",
    "nmap -sX {target}",
    "nmap -sY {target}",
    "nmap -sZ {target}",
    "nmap -Pn {target}",
    "nmap -n {target}",
    "nmap -R {target}",
    "nmap --dns-servers 8.8.8.8 {target}",
    "nmap -p 80 {target}",
    "nmap -p 1-65535 {target}",
    "nmap -p- {target}",
    "nmap --top-ports 100 {target}",
    "nmap -F {target}",
    "nmap -r {target}",
    "nmap --open {target}",
    "nmap -T0 {target}",
    "nmap -T1 {target}",
    "nmap -T2 {target}",
    "nmap -T3 {target}",
    "nmap -T4 {target}",
    "nmap -T5 {target}",
    "nmap -O {target}",
    "nmap --osscan-guess {target}",
    "nmap --fuzzy {target}",
    "nmap -sV {target}",
    "nmap --version-intensity 9 {target}",
    "nmap --version-all {target}",
    "nmap --script default {target}",
    "nmap --script safe {target}",
    "nmap --script vuln {target}",
    "nmap --script auth {target}",
    "nmap --script discovery {target}",
    "nmap --script malware {target}",
    "nmap --script intrusive {target}",
    "nmap --script http-* {target}",
    "nmap --script smb-* {target}",
    "nmap --script ftp-* {target}",
    "nmap --script dns-* {target}",
    "nmap --script ssl-* {target}",
    "nmap -v {target}",
    "nmap -vv {target}",
    "nmap -d {target}",
    "nmap -dd {target}",
    "nmap --reason {target}",
    "nmap --packet-trace {target}",
    "nmap --iflist",
    "nmap -6 {target}",
    "nmap --traceroute {target}",
    "nmap --data-length 50 {target}",
    "nmap --spoof-mac 00:11:22:33:44:55 {target}",
    "nmap -S 1.2.3.4 {target}",
    "nmap -D RND:10 {target}",
    "nmap -f {target}",
    "nmap --mtu 16 {target}",
    "nmap --scan-delay 5s {target}",
    "nmap --max-rate 100 {target}",
    "nmap --min-rate 10 {target}",
    "nmap --max-retries 3 {target}",
    "nmap --host-timeout 30m {target}",
    "nmap --script-updatedb",
    "nmap --stats-every 10s {target}",
    "nmap --min-hostgroup 50 {target}",
    "nmap --max-hostgroup 1024 {target}",
    "nmap --min-parallelism 10 {target}",
    "nmap --max-parallelism 100 {target}",
    "nmap --randomize-hosts {target}",
    "nmap --ipv6 {target}",
    # Specialized ping scan variations
    "nmap -sP 192.168.1.0/24",
    "nmap -sP 192.168.1.0/24 -n -v",
    "nmap -sP 192.168.1.0/24 -n -v --send-ip",
    "nmap -sP 192.168.1.0/24 -n -v --send-ip --system-dns",
    "nmap -sP 192.168.1.0/24 -n -v --send-ip --system-dns --dns-servers 8.8.8.8",
    "nmap -sP 192.168.1.0/24 -n -v --send-ip --system-dns --dns-servers 8.8.8.8 --dns-timeout 5s",
    "nmap -sP 192.168.1.0/24 -n -v --send-ip --system-dns --dns-servers 8.8.8.8 --dns-timeout 5s --max-parallelism 100",
    "nmap -sP 192.168.1.0/24 -n -v --send-ip --system-dns --dns-servers 8.8.8.8 --dns-timeout 5s --max-parallelism 100 --min-parallelism 10",
    "nmap -sP 192.168.1.0/24 -n -v --send-ip --system-dns --dns-servers 8.8.8.8 --dns-timeout 5s --max-parallelism 100 --min-parallelism 10 --max-retries 3",
    "nmap -sP 192.168.1.0/24 -n -v --send-ip --system-dns --dns-servers 8.8.8.8 --dns-timeout 5s --max-parallelism 100 --min-parallelism 10 --max-retries 3 --initial-rtt-timeout 500ms",
    "nmap -sP 192.168.1.0/24 -n -v --send-ip --system-dns --dns-servers 8.8.8.8 --dns-timeout 5s --max-parallelism 100 --min-parallelism 10 --max-retries 3 --initial-rtt-timeout 500ms --max-rtt-timeout 1200ms",
    "nmap -sP 192.168.1.0/24 -n -v --send-ip --system-dns --dns-servers 8.8.8.8 --dns-timeout 5s --max-parallelism 100 --min-parallelism 10 --max-retries 3 --initial-rtt-timeout 500ms --max-rtt-timeout 1200ms --min-rtt-timeout 100ms",
    "nmap -sP 192.168.1.0/24 -n -v --send-ip --system-dns --dns-servers 8.8.8.8 --dns-timeout 5s --max-parallelism 100 --min-parallelism 10 --max-retries 3 --initial-rtt-timeout 500ms --max-rtt-timeout 1200ms --min-rtt-timeout 100ms --max-scan-delay 10ms",
    "nmap -sP 192.168.1.0/24 -n -v --send-ip --system-dns --dns-servers 8.8.8.8 --dns-timeout 5s --max-parallelism 100 --min-parallelism 10 --max-retries 3 --initial-rtt-timeout 500ms --max-rtt-timeout 1200ms --min-rtt-timeout 100ms --max-scan-delay 10ms --min-scan-delay 5ms",
    "nmap -sP 192.168.1.0/24 -n -v --send-ip --system-dns --dns-servers 8.8.8.8 --dns-timeout 5s --max-parallelism 100 --min-parallelism 10 --max-retries 3 --initial-rtt-timeout 500ms --max-rtt-timeout 1200ms --min-rtt-timeout 100ms --max-scan-delay 10ms --min-scan-delay 5ms --max-hostgroup 256",
    "nmap -sP 192.168.1.0/24 -n -v --send-ip --system-dns --dns-servers 8.8.8.8 --dns-timeout 5s --max-parallelism 100 --min-parallelism 10 --max-retries 3 --initial-rtt-timeout 500ms --max-rtt-timeout 1200ms --min-rtt-timeout 100ms --max-scan-delay 10ms --min-scan-delay 5ms --max-hostgroup 256 --min-hostgroup 128",
    "nmap -sP 192.168.1.0/24 -n -v --send-ip --system-dns --dns-servers 8.8.8.8 --dns-timeout 5s --max-parallelism 100 --min-parallelism 10 --max-retries 3 --initial-rtt-timeout 500ms --max-rtt-timeout 1200ms --min-rtt-timeout 100ms --max-scan-delay 10ms --min-scan-delay 5ms --max-hostgroup 256 --min-hostgroup 128 --max-scan-attempts 5",
    "nmap -sP 192.168.1.0/24 -n -v --send-ip --system-dns --dns-servers 8.8.8.8 --dns-timeout 5s --max-parallelism 100 --min-parallelism 10 --max-retries 3 --initial-rtt-timeout 500ms --max-rtt-timeout 1200ms --min-rtt-timeout 100ms --max-scan-delay 10ms --min-scan-delay 5ms --max-hostgroup 256 --min-hostgroup 128 --max-scan-attempts 5 --min-scan-attempts 3",
    "nmap -sP 192.168.1.0/24 -n -v --send-ip --system-dns --dns-servers 8.8.8.8 --dns-timeout 5s --max-parallelism 100 --min-parallelism 10 --max-retries 3 --initial-rtt-timeout 500ms --max-rtt-timeout 1200ms --min-rtt-timeout 100ms --max-scan-delay 10ms --min-scan-delay 5ms --max-hostgroup 256 --min-hostgroup 128 --max-scan-attempts 5 --min-scan-attempts 3 --max-scan-delay-ms 10",
    "nmap -sP 192.168.1.0/24 -n -v --send-ip --system-dns --dns-servers 8.8.8.8 --dns-timeout 5s --max-parallelism 100 --min-parallelism 10 --max-retries 3 --initial-rtt-timeout 500ms --max-rtt-timeout 1200ms --min-rtt-timeout 100ms --max-scan-delay 10ms --min-scan-delay 5ms --max-hostgroup 256 --min-hostgroup 128 --max-scan-attempts 5 --min-scan-attempts 3 --max-scan-delay-ms 10 --min-scan-delay-ms 5",
]

def run_nmap(target):
    while True:
        clear_screen()
        color_print(f"--- Nmap Advanced Presets [{target if target else 'No Target'}] ---", "BLUE")
        print(" [1] Quick Standard Scan (nmap -A -T4)")
        print(" [2] Browse All Presets (100+ Commands)")
        print(" [3] Custom Command Input")
        print(" [0] Back to Main Menu")
        print("-" * 50)
        
        choice = get_input("Nmap")
        
        if choice == '1':
            if not target: target = get_input("Enter Target")
            run_cmd(["nmap", "-A", "-T4", target])
            input("\nPress Enter...")
        elif choice == '2':
            if not target: target = "target"
            for i, cmd in enumerate(NMAP_PRESETS):
                print(f" [{i:02}] {cmd.format(target=target)}")
            
            p_choice = get_input("Preset # (or ENTER to cancel)")
            if p_choice.isdigit() and int(p_choice) < len(NMAP_PRESETS):
                actual_target = get_input(f"Confirm Target [{target}]") or target
                final_cmd = NMAP_PRESETS[int(p_choice)].format(target=actual_target)
                run_cmd(final_cmd)
                input("\nPress Enter...")
        elif choice == '3':
            custom = get_input("Enter Full Nmap Command")
            if custom: run_cmd(custom)
            input("\nPress Enter...")
        elif choice == '0':
            break
