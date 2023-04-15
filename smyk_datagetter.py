from openpyxl import Workbook
from openpyxl import load_workbook
from bs4 import BeautifulSoup
import requests
from datetime import date 

def smyk_datagetter(x,main_window):
    if(x!=''):
        url=x
        try:
            result=requests.get(url)
        except requests.exceptions.RequestException:
            main_window.smyk_url.background_color = (1,0,0,0.1)
            return 0
        doc = BeautifulSoup(result.text, "html.parser")

        meta_tag=doc.find('meta', {'itemprop': 'price'})
        price=meta_tag.get('content')

        otherthings_tag=doc.find('meta',{'itemprop': 'name'})
        beta_tag=otherthings_tag.get('content').split(',')
        new_list = [string.replace(' ', '', 1) for string in beta_tag]

        brand=doc.find('meta',{'itemprop':'brand'} ).get('content')
        genre=new_list[1]
        category = new_list[2]
        volume=new_list[3]
        date_=date.today().strftime("%d.%m.%Y")

        wb = load_workbook("Parfume_prices_sk.xlsx")
        ws=wb.active
        ws.append([brand,genre,category,volume,float(price),url,date_])
        wb.save("Parfume_prices_sk.xlsx")
        main_window.smyk_url.background_color=(.5,1,.2,0.1)
    else:
        pass