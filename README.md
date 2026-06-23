# kurd_scanner 🚀

A blazing fast, multithreaded Python command-line tool for subdomain enumeration.

## ✨ Features
- High Speed: Uses ThreadPoolExecutor to scan multiple subdomains concurrently.
- Lightweight: Clean code with minimal dependencies.
- User Friendly: Beautiful and colored terminal output using colorama.

## 🛠️ Installation

1. Clone the repository or download the files:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/kurd_scanner.git](https://github.com/YOUR_USERNAME/kurd_scanner.git)
   cd kurd_scanner
pip install -r requirements.txt
python kurd_scanner.py -d example.com -w wordlist.txt
python kurd_scanner.py -d google.com -w subdomains_top5000.txt
