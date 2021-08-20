import requests

import time
import sqlite3
def sql_connector():
   con = sqlite3.connect('weather.db')
   cur = con.cursor()
   return con,cur
def create_table(con,cur):
   cur.execute('CREATE TABLE IF NOT EXISTS weather(name TEXT,datetime TEXT,TEMP TEXT)')
def insert_data(con,cur,data):
   cur.execute('INSERT INTO weather values(?,?,?)',tuple([v for k,v in data.items()]))
   con.commit()
def process_data(data):

   return{'city ':data['name'],'datetime ':time.ctime(int(data['dt'])),'temp':data['main']['temp']}

def get_wether_data(city='Tehran',appid='6022f89b92f3405e89dbec015491d4cd'):

   URL = "https://api.openweathermap.org/data/2.5/weather"

   location = "delhi technological university"

   PARAMS = {'q':city,'appid':appid}

   r = requests.get(url = URL, params = PARAMS )

   return process_data(r.json())
con,cur = sql_connector()
create_table(con,cur)

data_weather=(get_wether_data('Mashhad'))
insert_data(con,cur,data_weather)
print(data_weather)

