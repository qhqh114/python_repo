#coding = utf8

import requests
from bs4 import BeautifulSoup

res = requests.get('http://v.media.daum.net/v/20170615203441266')
soup = BeautifulSoup(res.content, 'html.parser')
paragraph_data = soup.find('p')

print(paragraph_data)












