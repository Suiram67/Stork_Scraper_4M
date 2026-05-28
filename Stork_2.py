import requests
import re
from bs4 import BeautifulSoup
import json
from datetime import datetime, timedelta

URL ="https://www.cigogne-management.com/fr/bank/cm/-/sie-97-xs3126645772"

rep = requests.get(URL)

idx = rep.text.find("103105")

print(rep.text[idx-300:idx+300])

matche = re.search(r"data:(\[\[.*?\]\])",rep.text)
date = json.loads(matche.group(1))
print(date)

with open("Scraper_2.csv","w",encoding = "utf-8") as l:
    for a,b in date:
        key_dico = datetime.fromtimestamp(a/1000)+timedelta(hours=2)
        ligne = f"{key_dico};{str(b)}\n"
        l.write(ligne)