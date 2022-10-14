import re
import requests
from bs4 import BeautifulSoup

def sangrok1():
    url = "http://dgucoop.dongguk.edu/mobile/menu.html?code=7"
    res = requests.get(url)
    res.encoding = None
    html = res.text

    bs = BeautifulSoup(html, "html.parser")

    tags_td = bs.findAll("td")
        
    if tags_td[3].text == None :
        menu = "현재 상록원 1층 생활협동조합에 등록된 메뉴가 없습니다."
    else :
        menu = "======= 상록원1층 =======\n"+"———"+tags_td[1].text+"———\n"
        for i in range(3, len(tags_td), 2) :
            text = tags_td[i].text
            if len(text) == 0:
                continue
            menu = menu + text + " " + "\n"
    return menu