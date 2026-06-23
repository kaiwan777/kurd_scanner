# kurd_scanner 🚀

A blazing fast, multithreaded Python command-line tool for subdomain enumeration.

## ✨ Features
* High Speed: Uses ThreadPoolExecutor to scan multiple subdomains concurrently.
* Lightweight: Clean code with minimal dependencies.
* User Friendly: Beautiful and colored terminal output using colorama.
* Automated Setup: Comes with an easy installation script.

---

## 📥 Installation

Open your terminal (e.g., in Kali Linux) and run the following commands one by one:

### 1. Clone the repository
```bash
# 1. git clone [https://github.com/kaiwan777/kurd_scanner.git](https://github.com/kaiwan777/kurd_scanner.git)

# 2. Move into project directory
 cd kurd_scanner

# 3. Give execution permission to the install
chmod +x install.sh

# 4. Run the installation script
./install.sh

# 5. 🏃‍♂️ Usage
After a successful installation, you can start scanning any domain by running:
python3 kurd_scanner.py -d google.com -w wordlist.txt

# 6. 💾 Saving Output (Optional)
If you want to save the discovered live subdomains to a text file, use the ⁠-o⁠ flag:
python3 kurd_scanner.py -d google.com -w wordlist.txt -o results.txt
