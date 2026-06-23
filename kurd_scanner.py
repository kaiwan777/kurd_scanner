import requests
import argparse
from colorama import Fore, init
from concurrent.futures import ThreadPoolExecutor

# Initialize colorama for cross-platform colored terminal output
init(autoreset=True)


def check_single_subdomain(sub, domain):
    """Tests a single subdomain and prints if it is active (Status 200)."""
    sub = sub.strip()
    if not sub:
        return

    url = f"http://{sub}.{domain}"
    try:
        # 3-second timeout to prevent the script from hanging
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            print(f"{Fore.GREEN}[+] 200 OK      : {Fore.WHITE}{url}")
    except requests.RequestException:
        # Ignore connection errors, timeouts, and other exceptions
        pass


def scan_subdomains(domain, wordlist_path):
    """Reads the wordlist and manages concurrent execution using ThreadPoolExecutor."""
    print(f"\n{Fore.CYAN}🚀 Starting subdomain scan on: {Fore.YELLOW}{domain}")
    print(f"{Fore.CYAN}📁 Using wordlist: {Fore.YELLOW}{wordlist_path}")
    print(Fore.MAGENTA + "-" * 55)

    try:
        with open(wordlist_path, 'r') as file:
            subdomains = file.read().splitlines()
    except FileNotFoundError:
        print(f"{Fore.RED}[-][Error] The file '{wordlist_path}' was not found.")
        return

    # ThreadPoolExecutor manages 10 parallel workers for high-speed scanning
    with ThreadPoolExecutor(max_workers=10) as executor:
        # Submit all subdomains to the thread pool concurrently
        futures = [executor.submit(check_single_subdomain, sub, domain) for sub in subdomains]

    print(Fore.MAGENTA + "-" * 55)
    print(f"{Fore.GREEN}✅ Scan Completed Successfully!")


if __name__ == "__main__":
    # Set up command-line arguments
    parser = argparse.ArgumentParser(
        description="Kurd Scanner - A high-speed, multithreaded subdomain enumeration tool.")
    parser.add_argument("-d", "--domain", required=True, help="Target domain to scan (e.g., google.com)")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to the wordlist file")
    parser.add_argument("-o", "--output", required=False, help="Save output to a text file")
    args = parser.parse_args()
    scan_subdomains(args.domain, args.wordlist)