from bs4 import BeautifulSoup
import urllib3
import json

email = 'zenotan@outlook.com'
url = 'http://www.adidas.nl'
http = urllib3.PoolManager()
header = {
        'User-Agent': 'My User Agent 1.0',
        'From': email
}

res = http.request('GET',url,headers=header)
soup = BeautifulSoup(res.data, "html.parser")
products = json.loads((soup))['products']
print(products)
