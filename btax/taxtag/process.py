import numpy as np
import pandas as pd
import re


import transformers
import spacy

from scrape import get_res,get_numac_numbers,scrape_numac,create_numac_links
from summary import summarise,tagging,create_tags,clean_dataframe
from models import Article



DATE='2022-06-10'


res = get_res(DATE)
numacs=get_numac_numbers(res.text)
numac_links=create_numac_links(numacs,DATE)
nl_list=scrape_numac(numac_links)

nl_list=nl_list[0:3]

#print(nl_list)

#SUMMARY

summary=summarise(nl_list)
nltags=create_tags(summary)



data = pd.DataFrame(
    {'date':DATE,
    'numac':numacs,
    'link':numac_links,

    'nl_text':nl_list,
      
        'nl_sum': summary,
     'nl_tags': nltags
    })


data=clean_dataframe(data)

print(data)





# class Article(models.Model):
#     date = models.DateField()
#     numac = models.CharField(max_length=15)
#     link=models.CharField(max_length=150)
#     nl_text=models.TextField()
#     nl_sum=models.TextField()
#     nl_tags=models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
