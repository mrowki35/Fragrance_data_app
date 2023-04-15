from openpyxl import Workbook
from openpyxl import load_workbook
from bs4 import BeautifulSoup
import requests
from datetime import date 
import re

def douglas_datagetter(x,main_window):
    if(x!=''):
        url=x
        try:
            result=requests.get(url)
        except requests.exceptions.RequestException:
            main_window.douglas_url.background_color = (1,0,0,0.1)
            return 0
        doc = BeautifulSoup(result.text, "html.parser")

        selected_button=doc.find('input', {'checked': True})
        try:
            current_id = selected_button.get('id')
            info_tag=doc.find('input',{'id':current_id}).parent
        except AttributeError:
            info_tag=doc
        try:
            price=info_tag.find('div', {'class':'product-price__discount product-price__discount product-price__discount--discount-color'}).find('span',{'class':"product-price__price"}).text.replace('zł','').replace(',',".")
        except AttributeError:
            price=info_tag.find('span',{'class':"product-price__price"}).text.replace('zł','').replace(',',".")

        volume=info_tag.find('div' ,{'class':"product-detail__variant-name"}).text
        brand=doc.find('span' ,{'class':"brand-logo__text brand-logo__text--dynamic"}).text
        genre=doc.find(['div'],{'class',"second-line"}).text
        category=doc.find('div',{'class':"third-line"}).text
        date_=date.today().strftime("%d.%m.%Y")

        wb=load_workbook("Parfume_prices_douglas.xlsx")
        ws=wb.active
        ws.append([brand,genre,category,volume,float(price.replace('\xa0','').strip()),url,date_])
        wb.save("Parfume_prices_douglas.xlsx")
        main_window.douglas_url.background_color=(.5,1,.2,0.1)
    else:
        pass






