#!/bin/bash

echo -e "\e[1;36m[*] Starting Kurd Scanner Installation...\e[0m"

echo -e "\e[1;33m[*] Installing required Python libraries...\e[0m"
pip3 install -r requirements.txt --break-system-packages

echo -e "\e[1;33m[*] Downloading a powerful 5000-word wordlist...\e[0m"
wget -q --show-progress https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/DNS/subdomains-top1million-5000.txt -O wordlist.txt

echo -e "\e[1;32m[+] Installation Completed Successfully! 🚀\e[0m"
echo -e "\e[1;37m[*] You can now run the tool using:\e[0m"
echo -e "    python3 kurd_scanner.py -d example.com -w wordlist.txt"