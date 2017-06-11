
import urllib
from bs4 import BeautifulSoup
from urllib.request import urlopen
quote_page = ["http://www.bloomberg.com/quote/SPX:IND","http://www.bloomberg.com/quote/CCMP:IND"]
data = []
for pg in quote_page:
  page = urlopen(pg)
  soup = BeautifulSoup(page, "html.parser")
  name_box = soup.find("h1", attrs={"class": "name"})
  name = name_box.text.strip() 
  price_box = soup.find("div", attrs={"class":"price"})
  price = price_box.text
  data.append((name, price))
import csv
from datetime import datetime
with open("index.csv", "a") as csv_file:
 writer = csv.writer(csv_file)
 for name, price in data:
  writer.writerow([name, price, datetime.now()])
