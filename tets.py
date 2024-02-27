import psycopg2
def select(id):
    qwery = f"""SELECT id, login, password FROM public.logins {id}; """
    cursor.execute(qwery)
    data = cursor.fetchall()
    return data

def update(id, login, password):
    qwery = f"""UPDATE public.logins SET {login} {password} {id}; """
    cursor.execute(qwery)
    con.commit()
    return 'Mission completed'

def insert(login, password):
    qwery = f"""INSERT INTO public.logins(login, password) VALUES ({login}, {password});"""
    cursor.execute(qwery)
    con.commit()
    return 'Mission completed'

def delete(id):
    qwery = f"""DELETE FROM public.logins {id};"""
    cursor.execute(qwery)
    con.commit()
    return 'Mission completed'

con = psycopg2.connect(dbname='test', user='postgres', password='Q1w2e3r4', host='localhost')
cursor = con.cursor()
id = "WHERE id=3"
print(delete(id))
print(select(''))

import time
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s = Service('C:/cw/chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get("https://www.kinopoisk.ru/lists/movies/top250/")
time.sleep(10)
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')
soup.find('div', class_="base-movie-main-info_mainInfo__ZL_u3")
print(soup.find('div', class_="desktop-list-main-info_secondaryTitleSlot__mc0mI").text)




