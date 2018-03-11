import requests


url = 'http://m.ip138.com/ip.asp?ip='
try:
    r = requests.get(url+'202.206.88.24')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print('fail')
