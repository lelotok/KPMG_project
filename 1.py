import pandas as pd
import sys
sys.setrecursionlimit(10000)
data=pd.read_csv('./data/KPMG _Tax_Case_Data _Set.csv')

import requests
from bs4 import BeautifulSoup
import csv

links=list(data['Link NL'])

nl_list=[]
for a in links:
    k=""
    try:

        res = requests.get(a)
        soup_data = BeautifulSoup(res.text, 'html.parser')
        
        k=soup_data.find_all('body')
        nl_list.append(k)
        
    except:
        k=""
        nl_list.append(k)
    with open("4.csv", 'a',encoding="utf-8") as f:
                    write = csv.writer(f)
                    write.writerow(k)

data["nli"]=nl_list
data.to_csv("56.csv")