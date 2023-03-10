from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
from bs4 import BeautifulSoup
import requests
from datetime import date 


url = "https://www.notino.pl/jimmy-choo/urban-hero-gold-woda-perfumowana-dla-mezczyzn/"


result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")




prices = doc.find_all(id="pd-price")
parent=prices[0].parent
span = parent.find_all("span")
price = span[1].text.replace(",",".")
volume = span[0].text


brands = doc.find_all(id="pdHeader")
brands_parent = brands[0].parent
stamp = brands_parent.find_all("span")
genre = stamp[1].text
brand = stamp[0].text.replace(genre,"")
category = stamp[2].text
date=date.today().strftime("%d.%m.%Y")


wb = load_workbook("Parfume_prices_database.xlsx")
ws = wb.active

ws.append([genre,brand,category,volume,float(price),url,date])
wb.save("Parfume_prices_database.xlsx")