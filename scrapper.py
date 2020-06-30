import requests
from bs4 import BeautifulSoup
from pprint import pprint

URL = 'https://www.amazon.com/Dash-Mini-Maker-Individual-Breakfast/dp/B010TCP3SC/ref=sr_1_3?dchild=1&keywords=mini+maker&qid=1593550187&sr=8-3'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id='productTitle').get_text()
price = soup.find(id='priceblock_ourprice').get_text()
converted_price = price[0:5]


pprint(title.strip())
pprint(converted_price)
