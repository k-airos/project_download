# -*- coding: utf-8 -*-
import requests
import mysql.connector
from bs4 import BeautifulSoup
import sqlalchemy as db
from sqlalchemy import create_engine
import parsing as pars
from crontab import CronTab
import os
import subprocess


def update(name_of_category,user,passw):
    db_engine = create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.format(user, passw, host,dbname))
    con = db_engine.raw_connection()
    cur = con.cursor()
    try:
        cur.execute(f"SELECT * FROM {name_of_category} WHERE id=(SELECT max(id) FROM {name_of_category});")
        title = cur.fetchone()[1]
    except TypeError:
        f1 =open('FLAG1.txt','w')
        cur.execute(f"""
            CREATE TABLE IF NOT EXISTS {name_of_category} (
            id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
            title text,
            content text,
            attributes text,
            date text
            );""")
        bigger_limit = pars.find_last_page(name_of_category)
        less_limit = 1
        for i in range(bigger_limit,less_limit-1,-1):
            url = f"http://www.mchsmedia.ru/news/{i}/?category={name_of_category}"
            pars.category(url,name_of_category)
    else:
        topics = []
        HOST = "http://www.mchsmedia.ru"
        headers = {"User-Agent": "k_airos_user"}
        i = 1
        flag = True
        while flag:
            url = f"http://www.mchsmedia.ru/news/{i}/?category={name_of_category}"
            s = requests.Session()
            html = s.get(url,headers = headers)
            soup = BeautifulSoup(html.text,'html.parser')
            items = soup.find_all("div", class_="cl-item clearfix")
            for item in items:
                if(title in item.get_text()):
                    flag = False
                    break
                if flag == True:
                    topics.append(
                        {
                            "text":item.find("div",class_="cl-item-title").find("a").get_text(),
                            "link":HOST + item.find('a').get("href"),
                            "datatime":item.find("div",class_="cl-item-date").get_text()
                        }
                    )
            i+=1
        for i in reversed(topics):
            attributes,text = pars.get_from_item(i['link'])
            buff = i['datatime'].find('• ')
            bufs = i['datatime'][buff+2:]
            bufs = bufs[:11]
            if(any(substring in text.lower() for substring in ["пожар","возгоран","огонь"]) and "гарнизон" not in text.lower()):
                attributes += " пожар"   
            if(any(substring in text.lower() for substring in ["газ","хлопок","взрыв"])):
                attributes += " взрыв газа"
            if(any(substring in text.lower() for substring in ["утечка"])):
                attributes += " утечка газа"
            if(any(substring in text.lower() for substring in ["теракт","террор"])):
                attributes += " теракт"
            if (any(substring in text.lower() for substring in ["дтп"])):
                attributes += " дтп"
            if (any(substring in text.lower() for substring in ["наводн","потоп","подтоп","воды"])):
                attributes += " затопление"
            if ("вирус" in text.lower()):
                attributes += " эпидемии"
            con = db_engine.connect()
            con.execute(f"INSERT INTO {name_of_category} (title,content,attributes,date) VALUES(%s,%s,%s,%s);",(i['text'],text,attributes,bufs))
        topics = []

host = "127.0.0.1"
dbname = "MoES"

def updateForCron(myTable):
 
    my_cron = CronTab(user=True)
    my_cron.remove_all()
    if(myTable == "5 min"):
        job = my_cron.new(command=f'cd {os.path.abspath(os.path.join(__file__ ,"../"))} && {os.path.abspath(os.path.join(__file__ ,"../env/bin/python"))} {os.path.abspath("update.py")} command arg')
        job.minute.every(5)
    if(myTable == "30 min"):
        job = my_cron.new(command=f'cd {os.path.abspath(os.path.join(__file__ ,"../"))} && {os.path.abspath(os.path.join(__file__ ,"../env/bin/python"))} {os.path.abspath("update.py")} command arg')
        job.minute.every(30)
    if(myTable == "1 hour"):
        job = my_cron.new(command=f'cd {os.path.abspath(os.path.join(__file__ ,"../"))} && {os.path.abspath(os.path.join(__file__ ,"../env/bin/python"))} {os.path.abspath("update.py")} command arg')
        job.hour.every(1)
    if(myTable == "1 day"):
        job = my_cron.new(command=f'cd {os.path.abspath(os.path.join(__file__ ,"../"))} && {os.path.abspath(os.path.join(__file__ ,"../env/bin/python"))} {os.path.abspath("update.py")} command arg')
        job.day.every(1)
    if(myTable == "1 week"):
        job = my_cron.new(command=f'cd {os.path.abspath(os.path.join(__file__ ,"../"))} && {os.path.abspath(os.path.join(__file__ ,"../env/bin/python"))} {os.path.abspath("update.py")} command arg')
        job.day.every(7)
    
    # job = my_cron.new(command='echo 32423 > /home/kirill/Desktop/individual_pr/blalbla.log')
    # job.minute.every(1)
    my_cron.write()

if __name__ == "__main__":
    with open('text.txt','r') as f:
        a = f.read()
        a = a.split('..')
        user = a[0]
        passw = a[1]
        update("forecasts",user,passw)
        update("mchs_news",user,passw)
        update("regional_news",user,passw)
        update("incidents",user,passw)