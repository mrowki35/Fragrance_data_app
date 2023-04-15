from openpyxl import Workbook
from openpyxl import load_workbook
from bs4 import BeautifulSoup
import requests
from datetime import date 
import json

def superpharm_datagetter(x,main_window):
    if(x!=''):
        url=x
        try:
            result=requests.get(url)
        except requests.exceptions.RequestException:
            main_window.superph_url.background_color = (1,0,0,0.1)
            return 0
        doc = BeautifulSoup(result.text, "html.parser")

        price_tag=doc.find("span",{"data-price-type":"finalPrice"}).text
        price=price_tag.split()[0].replace(",",".").strip()
        brand=doc.find("div",{"class":"producer-logo"}).find('a')['title']

        #do poprawienia jesli if nie istnieje to znajdz to w og w tilte
        obj = doc.find(["h2", "h3"], {"data-element":"main"}).text
        category_tag=doc.find("div",{"class":"sub-title"}).text.replace("\n","")
        category=category_tag.replace("dla mężczyzn","").strip()
        genre=obj.replace(category_tag,"").replace("-","").replace(brand,"").strip()
        date_=date.today().strftime("%d.%m.%Y")

        temp_brand=brand.lower()
        temp_genre=genre.lower()

        volume=doc.find("span",{"data-ui-id":"page-title-wrapper"}).text.lower().replace(temp_brand,"",1).replace(temp_genre,"").strip()

        wb=load_workbook("Parfume_prices_superph.xlsx")
        ws=wb.active

        ws.append([brand,genre,category,volume,float(price),url,date_])
        wb.save("Parfume_prices_superph.xlsx")
        main_window.superph_url.background_color=(.5,1,.2,0.1)
    else:
        pass