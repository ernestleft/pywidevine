import requests

headers = {
    'authority': 'cwip-shaka-proxy.appspot.com',
    'accept': '*/*',
    'accept-language': 'en,es-ES;q=0.9,es;q=0.8',
    'origin': 'https://bitmovin.com',
    'referer': 'https://bitmovin.com/',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded',
}

data = '\b\x04'

response = requests.post('https://cwip-shaka-proxy.appspot.com/no_auth', headers=headers, data=data)
