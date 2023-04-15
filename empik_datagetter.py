from openpyxl import Workbook
from openpyxl import load_workbook
from bs4 import BeautifulSoup
import requests
from datetime import date 


def empik_datagetter(x,main_window):
    if(x!=''):
        url = x
        try:
            result=requests.get(url)
        except requests.exceptions.RequestException:
            main_window.empik_url.background_color = (1,0,0,0.1)
            return 0
        doc = BeautifulSoup(result.text, "html.parser")

        price_tag=doc.find("div", {"class":"productPriceInfo__wrapper"}).text
        price=price_tag.replace(',','.').split()[0].strip()

        info_tag=doc.find(['h1','h2','h3'],{'itemprop':'name'}).text.strip().split(',')


        brand=info_tag[0].strip()
        genre=info_tag[1].strip()
        category=info_tag[2].strip()
        volume=info_tag[3].strip()
        date_=date.today().strftime("%d.%m.%Y")


        wb=load_workbook("Parfume_prices_empik.xlsx")
        ws=wb.active

        ws.append([brand,genre,category,volume,float(price),url,date_])
        wb.save("Parfume_prices_empik.xlsx")
        main_window.empik_url.background_color=(.5,1,.2,0.1)
    else:
        pass