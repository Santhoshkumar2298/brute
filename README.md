# Brute Tool

## Overview
A simple Python tool for penetration testing, designed for ethical purpose to perform brute-force attacks.

## Features
- Supports both GET and POST HTTP methods.
- Utilizes a wordlist for username and password combinations.

## Prerequisites
- Python 3.x
- requests library

## Usage
## 1. Clone the repository:
    git clone https://github.com/Santhoshkumar2298/brute.git
    cd brute-force-tool
## 2. Install Dependencies:
    pip install -r requirements.txt
## 3. Run the Tool:
    python brute_force.py -w path/to/wordlist.txt -t http://target.com/login -m post
    
    For Help:
    
    python brute_force.py -h [--help]
## 4. Command-line Arguments
    -w or --wordlist: Path to the wordlist file (required).
    -t or --target: Target URL (required).
    -m or --method: HTTP method (get or post, required).
## 5. Example:
    python brute_force.py -w wordlists/common_passwords.txt -t http://example.com/login -m post
  
## Warning
This tool is intended for educational and penetration testing purposes only. Unauthorized use is illegal.

## Disclaimer
The author is not responsible for any misuse or damage caused by this tool. Use it responsibly and ethically.

