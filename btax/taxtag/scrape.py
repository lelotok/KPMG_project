import numpy as np
import pandas as pd
import re

import requests
from bs4 import BeautifulSoup


import string
import unidecode

MAINLINK='https://www.ejustice.just.fgov.be/cgi/summary_body.pl?language=nl&pub_date='
DETAILLINK='https://www.ejustice.just.fgov.be/cgi/article_body.pl?language=nl&caller=summary&pub_date='



def get_res(date):
    '''
    Function to return resource for beautifulsoup date in YYYY-MM-DD format
    '''
    return requests.get(MAINLINK + date)


def get_numac_numbers(res:str):
    '''
    Function to get numac numbers from the res object
    '''
    _numacs=[]
    soup = BeautifulSoup(res, 'html.parser')
    try:
        value = soup.find_all('input', {'name': 'numac'})
      
    except Exception as e:
        print("Got unhandled exception %s" % str(e))
    for v in value:
        _numacs.append(v['value'].strip())
    return _numacs


def create_numac_links(_numacs:list,date):
    '''
    Function to get numac links for specified date (date in YYYY-MM-DD format)
    '''
    links=[]

    for _a in _numacs:
        link = f"{DETAILLINK}{date}&numac={_a}"
        links.append(link)
    return links



def clean(_a:str):
    '''
    Function to clean scraped article
    '''
    d=re.sub(r'(?<=[.,;,:])(?=[^\s])', r' ', _a)
    
    document_test= unidecode.unidecode(d)
    document_test = document_test.replace('\\n', ' ').replace('\n', ' ').replace('\t',' ').replace('\\', ' ').replace('. com', '.com')

    pattern = re.compile(r'\s+') 
    Without_whitespace = re.sub(pattern, ' ', document_test)
    # There are some instances where there is no space after '?' & ')', 
    # I am replacing these with one space so that It will not consider two words as one token.
    document_test = Without_whitespace.replace('?', ' ? ').replace(')', ') ')
    
 
    document_test = re.sub(r"[^a-zA-Z0-9:$-,%.?!]+", ' ', document_test) 
   
    # Remove Mentions
    document_test = re.sub(r'@\w+', '', document_test)
    #document_test = re.sub(r"[^a-zA-Z:$-,%.?!]+", ' ', document_test)

    return document_test

def scrape_numac(_numac_links:list):
    '''
    Function to scrape articles 
    '''
    _count=0 # to check which line
    nl_list=[]
    for a in _numac_links:
        _count+=1
        res = requests.get(a)
        soup = BeautifulSoup(res.text, 'html.parser')
        for sup in soup.find_all('sup'):
            sup.unwrap()
    
        
        text = soup.get_text(separator=" ").strip()
        text=text.replace('\n',"")
        print(text)

        lst=text.split('Numac :')[1].split(text.split('Numac :')[2])
    

        article=lst[1].split('begin eerste woord laatste')[0].strip()
        article=clean(article)
        nl_list.append(article)
        print(_count)
    return nl_list


