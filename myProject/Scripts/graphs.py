import plotly.graph_objs as go
import sqlalchemy as db
from sqlalchemy import create_engine
import mysql.connector
import pandas as pd
import datetime

def DfForGraph(myDateFrom,myDateTo,myTable):
    host = "127.0.0.1"
    user = "kairos"
    passw = "1"
    dbname = "MoES"
    mysql_engine = create_engine('mysql+mysqlconnector://{0}:{1}@{2}'.format(user, passw, host))

    mysql_engine.execute("CREATE DATABASE IF NOT EXISTS {0} DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;".format(dbname))

    db_engine = create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.format(user, passw, host,dbname))

    meta = db.MetaData()
    con = db_engine.raw_connection()
    cur = con.cursor()
    cur.execute(f"""
    SELECT {myTable}.attributes 
    FROM {dbname}.{myTable} 
    WHERE ((STR_TO_DATE({myTable}.date,'%d.%m.%Y ') >= STR_TO_DATE("{myDateFrom}",'%Y-%m-%d')) 
    and (STR_TO_DATE({myTable}.date,'%d.%m.%Y ') <= STR_TO_DATE("{myDateTo}",'%Y-%m-%d')));
    """)
    a = myDateFrom+'/'+myDateTo
    
    mydict = {
        "Происшествия":["Возгорания","Утечки газа","Теракты","ДТП","Затопления","Эпидемии"],
        "Количество":[0,0,0,0,0,0],
        "Даты":[a,a,a,a,a,a],
    }
    for i in cur:
        if ("пожар" in i[0]):
            mydict["Количество"][0] += 1
        if ("утечка газа" in i[0]):
            mydict["Количество"][1] += 1
        if ("теракты" in i[0]):
            mydict["Количество"][2] += 1
        if ("дтп" in i[0]):
            mydict["Количество"][3] += 1
        if ("затопление" in i[0]):
            mydict["Количество"][4] += 1
        if ("эпидемии" in i[0]):
            mydict["Количество"][5] += 1

    

    df = pd.DataFrame.from_dict(mydict)
    df = df.sort_values(by=['Количество'],ascending=False)
    return df


