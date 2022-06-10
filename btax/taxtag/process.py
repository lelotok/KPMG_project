import numpy as np
import pandas as pd
import re


import transformers
import spacy

from scrape import get_res,get_numac_numbers,scrape_numac,create_numac_links
from summary import summarise


SIMILARITY=0.80
DATE='2022-01-05'


res = get_res(DATE)
numacs=get_numac_numbers(res.text)
numac_links=create_numac_links(numacs,DATE)
nl_list=scrape_numac(numac_links)

#print(nl_list)

#SUMMARY

summary=summarise(nl_list)


tags='aanslagjaar covid arbeidsongeschiktheidsuitkeringen bedrijfsinkomsten bedrijfskosten bedrijfstoeslag bedrijfsvoorheffing belasting belastingverdragen belastingverhoging'\
     'belastingvermindering belastingvoet belastingvoordeel belastingvrije beroepsinkomsten beroepskosten bezoldiging btw derdebetalersregeling dienstverplichtingen erfbelasting'\
     'financieringskosten heffing inkomsten inkomstenderving investeringsaftrek kapitaalaflossingen kapitaalvermindering kostenvermindering omzetbelasting personenbelasting'\
     'prestatievergoeding rechtspersonenbelasting registratierechten schenkbelasting socialezekerheidsbijdragen solidariteitsbijdrage uitbetalingsinstelling vennootschapsbelasting'\
     'verminderingen vervangingsinkomsten voorafbetalingen voorbelasting voorheffing vrijstellingsregeling waardevermindering werkgeversbijdrage werkingskosten zekerheidsbijdragen'\
     'invaliditeit verzekering'


nlp = spacy.load("nl_core_news_lg")
real_tags=nlp(tags)

def tagging(real_tags,summary_tags):
    summary_tag_list={}

    for _a in summary_tags:
        
        for token in real_tags:
            q=token.similarity(_a)
        
            if q > SIMILARITY:
                
                #add token to dict
                summary_tag_list[token]=q
                #print(_a,token,_a.similarity(token))
    return summary_tag_list

keys=[]
t=0
for a in summary:
    print(t)
    text=a.lower()
    summary_tags=nlp(text)      
    
    summary_tag_list=tagging(real_tags,summary_tags)
    keys.append(summary_tag_list)
    t=t+1

data = pd.DataFrame(
    {'date':DATE,
    'numac':numacs,
        'nllink':numac_links,
        'summary': summary,
     'nltags': keys
    })

import numpy as np
data['nltags']=data['nltags'].astype(str)
data['nltags']=data["nltags"].str.strip('{}')
data['nltags'] = data['nltags'].replace('',np.nan,regex = True)
data.dropna(subset = ["nltags"], inplace=True)

