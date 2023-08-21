#4.Build a python script which works like gobuster
# (takes ip address/domain as an argument and a wordlist, and enumerates to try and find if that directory exists, example,
# python3 your_script.py 10.10.10.10 wordlist.txt

import requests
import sys

def check_words_in_url(url, wordlist):
    for word in wordlist:
        target_url = url +"/" + word
        response = requests.get(target_url)

        if response.status_code == 200:
            print(f"Status 200 for word: {target_url}")

if len(sys.argv) != 3:
    print("Usage: python script_name.py <url> <wordlist>")
    sys.exit(1)

url = sys.argv[1]
wordlist_path = sys.argv[2]

try:
    with open(wordlist_path, "r") as f:
        wordlist = [line.strip() for line in f]
except FileNotFoundError:
    print("Wordlist file not found.")
    sys.exit(1)

check_words_in_url(url, wordlist)
