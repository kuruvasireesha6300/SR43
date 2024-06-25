import requests
from bs4 import BeautifulSoup
import csv
import pandas as p
url="https://www.flipkart.com/search?q=mobiles"
r=requests.get(url)

soup=BeautifulSoup(r.content,"html.parser")

titles=soup.find_all('div',class_='_1TmfNK')
print(titles)