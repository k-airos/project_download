#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import mysql.connector
from bs4 import BeautifulSoup
import sqlalchemy as db
from sqlalchemy import create_engine
import parsing as pars
import update as up

    


# ПЕРЕДЕЛАЙ НА find конструкции с in



# Main part of programm (POTOM OBYEDINI V 2 BLOKA 1 - SOZDANIE .bd 2 - POPOLNENIE)
# con = sqlite3.connect('MoES.db')
def Fill(less_limit,bigger_limit,name_of_category,user,passw):
    host = "127.0.0.1"
    dbname = "MoES"
    mysql_engine = create_engine('mysql+mysqlconnector://{0}:{1}@{2}'.format(user, passw, host))


    mysql_engine.execute("CREATE DATABASE IF NOT EXISTS {0} DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;".format(dbname))


    db_engine = create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.format(user, passw, host,dbname))

    meta = db.MetaData()
    con = db_engine.raw_connection()
    cur = con.cursor()
    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {name_of_category} (
            id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
            title text,
            content text,
            attributes text,
            date text
        );""")
    cur.close()
    con.close()


    str_num = pars.find_last_page(name_of_category)
    # less_limit = 2
    # bigger_limit = 5
    for i in range(bigger_limit,less_limit-1,-1):
        url = f"http://www.mchsmedia.ru/news/{i}/?category={name_of_category}"
        pars.category(url,name_of_category,user,passw)
    # up.update(name_of_category)

    con.close()







