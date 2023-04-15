from openpyxl import Workbook
from openpyxl import load_workbook
from bs4 import BeautifulSoup
import requests
from datetime import date 
import json

def hebe_datagetter(x,main_window):
    if(x!=''):
        url = x
        try:
            result=requests.get(url)
        except requests.exceptions.RequestException:
            main_window.hebe_url.background_color = (1,0,0,0.1)
            return 0
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        json_obj=json.loads(doc.find("script",type="application/ld+json").string)
        vol_and_cat_tag=json_obj["disambiguatingDescription"]

        price = json_obj['offers']['lowPrice']
        brand =json_obj['brand'][0]['name']
        genre=json_obj['name'].replace(brand,"").strip()
        volume=vol_and_cat_tag.split(',')[1].strip()
        category=vol_and_cat_tag.split(",")[0].replace("męska","").replace("unisex","").strip()
        date_=date.today().strftime("%d.%m.%Y")

        wb=load_workbook("Parfume_prices_hebe.xlsx")
        ws=wb.active

        ws.append([brand,genre,category,volume,float(price),url,date_])
        wb.save("Parfume_prices_hebe.xlsx")
        main_window.hebe_url.background_color=(.5,1,.2,0.1)
    else:
        pass


