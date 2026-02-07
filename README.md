# AaayafujNSM Modular CLI Suite

```text
     /.\                                        .|';                    '||\   ||` .|'''|  '||\   /||` 
    // \\                                       ||               ''      ||\\  ||  ||       ||\\.//||  
   //...\\     '''|.   '''|.  '||  ||`  '''|.  '||'  '||  ||`    || ---  || \\ ||  `|'''|,  ||     ||  
  //     \\   .|''||  .|''||   `|..||  .|''||   ||    ||  ||     ||      ||  \\||   .   ||  ||     ||  
.//       \\. `|..||. `|..||.      ||  `|..||. .||.   `|..'|.    ||     .||   \||.  |...|' .||     ||. 
                                ,  |'                            ||                                    
                                 ''                           `..|'                                  
```

## Overview
AaayafujNSM is a professional-grade, modular security toolkit developed in Python. It consolidates industry-standard security tools into a single, intuitive command-line interface. Designed for penetration testers and network administrators, it streamlines scanning, vulnerability assessment, and information gathering.

## Key Features
- **Advanced Nmap Integration**: 100+ scan presets including aggressive service detection, stealth scans, and specialized ping variations.
- **SQLMap Automation**: 60+ pre-configured commands for automated database vulnerability testing and exploitation.
- **Metasploit Search**: Quick-query interface for finding Metasploit modules, exploits, and payloads.
- **Enhanced OSINT**: Real-time geolocation and network intelligence gathering via IP-API.
- **DNS & WHOIS Lookup**: Comprehensive domain resolution and registration data retrieval.
- **Cross-Platform**: Full support for Linux (optimized for Kali/Debian) and Windows via Batch launcher.

## Installation

### 1. Installation via GitHub (Recommended)
You can install the suite directly from the official repository:

```bash
# Clone the repository
git clone https://github.com/aaayafuj51-AYFJ/Aaayafuj_SMM.py.git

# Enter the directory
cd Aaayafuj_SMM.py

# Run the automated installer (Linux only)
sudo bash scripts/install_tools.sh

# Run the tool
python3 AaayafujNSM.py
```

### 2. Manual Installation (Linux)
1. Download the source files.
2. Navigate to the project root.
3. Run: `sudo bash scripts/install_tools.sh`
4. Launch: `python3 AaayafujNSM.py`

### 3. Windows Installation
1. Ensure [Python 3.x](https://www.python.org/) is installed and added to your PATH.
2. Download and install [Nmap for Windows](https://nmap.org/download.html).
3. Execute `AaayafujNSM.bat` to launch the terminal interface.

## Quick Start
Once launched, use the numeric menu to navigate through the toolset. You can select pre-defined high-performance scan templates or enter custom commands directly within the interface.

## Project Structure
- `AaayafujNSM.py`: Main entry point.
- `AaayafujNSM.bat`: Windows command-line launcher.
- `menu.py`: Interactive TUI logic and navigation.
- `nmap_tool.py`: Nmap automation module.
- `sqlmap_tool.py`: SQLMap automation module.
- `scripts/install_tools.sh`: Automated dependency installer.

## Disclaimer
**AaayafujNSM is intended for authorized security testing and educational purposes only.** Unauthorized access to computer systems is illegal. Users are solely responsible for compliance with local, state, and federal laws. The developers assume no liability for misuse of this tool.
