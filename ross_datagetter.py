from openpyxl import Workbook
from openpyxl import load_workbook
from bs4 import BeautifulSoup
import requests
from datetime import date 
import json

def ross_datagetter(x,main_window):
    if(x!=''):
        url = x
        try:
            result=requests.get(url)
        except requests.exceptions.RequestException:
            main_window.ross_url.background_color = (1,0,0,0.1)
            return 0
        doc = BeautifulSoup(result.text, "html.parser")

        json_obj = json.loads(doc.find("script", type="application/ld+json").string)
        price = json_obj["offers"]["price"]
        info_tag = doc.find("meta", {"property":"og:site_name"})

        infolist=info_tag.get('content').split(",")
        new_list=[string.replace(' ', '', 1) for string in infolist[1:]]
        new_list.append(infolist[0])

        temporarylist=new_list[2].split("|")
        volume=temporarylist[0].strip()
        genre=new_list[0]
        category=new_list[1].split('dla')[0].strip()
        brand=new_list[3]
        date_=date.today().strftime("%d.%m.%Y")

        wb = load_workbook("Parfume_prices_ross.xlsx")
        ws=wb.active
        ws.append([brand,genre,category,volume,float(price),url,date_])
        wb.save("Parfume_prices_ross.xlsx")
        main_window.ross_url.background_color=(.5,1,.2,0.1)
    else:
        pass