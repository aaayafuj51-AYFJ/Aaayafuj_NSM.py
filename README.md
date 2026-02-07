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
AaayafujNSM is a professional-grade, modular security toolkit developed in Python. It consolidates industry-standard security tools into a single, intuitive command-line interface. 

## Installation

### 1. Installation via GitHub
```bash
git clone https://github.com/aaayafuj51-AYFJ/Aaayafuj_SMM.py.git
cd Aaayafuj_SMM.py
sudo bash scripts/install_tools.sh
python3 AaayafujNSM.py
```

### 2. Windows Installation
1. Install [Python 3.x](https://www.python.org/).
2. Run `AaayafujNSM.bat`.

## Troubleshooting
**Error: "Rust toolchain not found" or "pydantic-core failed"**
This happens when `pip` tries to compile a package from source because it can't find a compatible binary (wheel).
- **Fix:** The updated `install_tools.sh` handles this by upgrading `pip`, `setuptools`, and `wheel` before installing other dependencies. If manual fix is needed:
  ```bash
  python3 -m pip install --upgrade pip setuptools wheel
  ```

## Disclaimer
**AaayafujNSM is intended for authorized security testing and educational purposes only.** The developers assume no liability for misuse.
