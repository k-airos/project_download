import requests
from bs4 import BeautifulSoup
import sqlalchemy as db
from sqlalchemy import create_engine

def get_from_item(url):
    headers = {"User-Agent": "k_airos_user"}
    s = requests.Session()
    html = s.get(url,headers = headers)
    soup = BeautifulSoup(html.text,'html.parser')
    attributes = soup.find("div",class_="b-article-header__tags").get_text()
    try:
        text = soup.find("article", class_="e-insert-promo").get_text()
    except AttributeError:
        text = soup.find("div", class_="e-insert-promo").get_text()
    return attributes,text

def find_last_page(name_of_category):
    if name_of_category == "incidents":
        str_num = 2748 #for 04.06
    elif name_of_category == "mchs_news":
        str_num = 2375 #for 04.06
    elif name_of_category == "regional_news":
        str_num = 3024 #for 04.06
    elif name_of_category == "forecasts":
        str_num = 170 #for 04.06
    while True:
        r = requests.get(f'http://www.mchsmedia.ru/news/{str_num}/?category={name_of_category}')
        if(r.status_code!=200):
            break
        str_num+=1

    return str_num -1


def category(url,name_of_category,user,passw): #for filling 
    db_engine = create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.format(user, passw, host,dbname))
    con = db_engine.connect()
    topics = []
    HOST = "http://www.mchsmedia.ru"
    headers = {"User-Agent": "k_airos_user"}
    s = requests.Session()
    html = s.get(url,headers = headers)
    soup = BeautifulSoup(html.text,'html.parser')
    items = soup.find_all("div", class_="cl-item clearfix")
    for item in reversed(items):
        topics.append(
            {
                "text":item.find("div",class_="cl-item-title").find("a").get_text(),
                "link":HOST + item.find('a').get("href"),
                "datatime":item.find("div",class_="cl-item-date").get_text()
            }
        )

    for i in topics:
        attributes,text = get_from_item(i['link'])
        buff = i['datatime'].find('• ')
        bufs = i['datatime'][buff+2:]
        bufs = bufs[:11]
        if(any(substring in text.lower() for substring in ["пожар","возгоран","огонь"])and "гарнизон" not in text.lower()):
            attributes += " пожар"   
        if(any(substring in text.lower() for substring in ["утечка","газ","хлопок","взрыв"])):
            attributes += " утечка газа"
        if(any(substring in text.lower() for substring in ["теракт","террор"])):
            attributes += " теракт"
        if (any(substring in text.lower() for substring in ["дтп"])):
            attributes += " дтп"
        if (any(substring in text.lower() for substring in ["наводн","потоп","подтоп"])):
            attributes += " затопление"
        if ("вирус" in text.lower() and "корона" not in text.lower()):
            attributes += " эпидемии"
        con.execute(f"INSERT INTO {name_of_category} (title,content,attributes,date) VALUES(%s,%s,%s,%s);",(i['text'],text,attributes,bufs))
    topics = []
    con.close()

host = "127.0.0.1"
dbname = "MoES"