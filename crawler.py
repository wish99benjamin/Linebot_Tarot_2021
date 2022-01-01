import requests
from bs4 import BeautifulSoup

url = "https://www.tarnote.com/blog/%E5%A1%94%E7%BE%85%E7%89%8C%E7%BE%A9-the-fool-%E6%84%9A%E8%80%85"
def crawler(url, mode):
    string = ''
    enable = 0
    r = requests.get(url) #將網頁資料GET下來
    soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
    sel = soup.find_all(['p', 'h3']) #取HTML標中的 <div class="title"></div> 中的<a>標籤存入sel
    for s in sel:
        if mode == 1:
            if "可能代表的意義" in s.text or "意義如下" in s.text or "逆位牌義" in s.text:
                enable = 0
            if enable == 1:
                string += s.text
            if "正位牌義" in s.text:
                enable = 1
        else:
            if "塔羅牌的小建議" in s.text:
                enable = 0
            if enable == 1:
                string += s.text
            if "逆位牌義" in s.text:
                enable = 1
    string = string.replace(' ', '')
    print(string)
    return string
    
   
