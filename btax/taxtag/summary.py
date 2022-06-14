import transformers
import spacy
import pandas as pd
import numpy as np
import re


SIMILARITY=0.80

tags='aanslagjaar covid arbeidsongeschiktheidsuitkeringen bedrijfsinkomsten bedrijfskosten bedrijfstoeslag bedrijfsvoorheffing belasting belastingverdragen belastingverhoging'\
     'belastingvermindering belastingvoet belastingvoordeel belastingvrije beroepsinkomsten beroepskosten bezoldiging btw derdebetalersregeling dienstverplichtingen erfbelasting'\
     'financieringskosten heffing inkomsten inkomstenderving investeringsaftrek kapitaalaflossingen kapitaalvermindering kostenvermindering omzetbelasting personenbelasting'\
     'prestatievergoeding rechtspersonenbelasting registratierechten schenkbelasting socialezekerheidsbijdragen solidariteitsbijdrage uitbetalingsinstelling vennootschapsbelasting'\
     'verminderingen vervangingsinkomsten voorafbetalingen voorbelasting voorheffing vrijstellingsregeling waardevermindering werkgeversbijdrage werkingskosten zekerheidsbijdragen'\
     'invaliditeit verzekering'





undisputed_best_model = transformers.MBartForConditionalGeneration.from_pretrained(
    "ml6team/mbart-large-cc25-cnn-dailymail-nl-finetune"
)
tokenizer = transformers.MBartTokenizer.from_pretrained("facebook/mbart-large-cc25")
summarization_pipeline = transformers.pipeline(
    task="summarization",
    model=undisputed_best_model,
    tokenizer=tokenizer,
)
summarization_pipeline.model.config.decoder_start_token_id = tokenizer.lang_code_to_id[
    "nl_XX"
]

#Creating the summary with pretrained model and saving to a csv file in case an error and appending to dataframe 

def summarise(_nl_list:list):
    counter=0
    summary=[]
    for text in _nl_list:
        

        t= summarization_pipeline(
            text,
            do_sample=True,
            top_p=0.75,
            top_k=50,
            num_beams=4,
            min_length=50,
            early_stopping=True,
            truncation=True,
        )[0]["summary_text"]

        summary.append(t)

        counter=counter+1
        print(counter)
    return summary




nlp = spacy.load("nl_core_news_lg")


def tagging(real_tags,summary_tags):
    summary_tag_list={}

    for _a in summary_tags:
        
        for token in real_tags:
            q=round(token.similarity(_a),3)
        
            if q > SIMILARITY:
                
                #add token to dict
                summary_tag_list[token]=q
                #print(_a,token,_a.similarity(token))
    return summary_tag_list



def create_tags(summary:list):
    real_tags=nlp(tags)
    keys=[]
    t=0
    for a in summary:
        print(t)
        text=a.lower()
        summary_tags=nlp(text)      
        
        summary_tag_list=tagging(real_tags,summary_tags)
        dict1 = summary_tag_list
        sorted_dict = {}
        sorted_keys = sorted(dict1, key=dict1.get,reverse=True)  # [1, 3, 2]

        for w in sorted_keys:
            sorted_dict[w] = dict1[w]

        first5pairs = {k: sorted_dict[k] for k in list(sorted_dict)[:5]}


        keys.append(first5pairs)
        
        t=t+1
    return keys


def clean_dataframe(data):

    data['nl_tags']=data['nl_tags'].astype(str)
    data['nl_tags']=data["nl_tags"].str.strip('{}')
    data['nl_tags'] = data['nl_tags'].replace('',np.nan,regex = True)
    data.dropna(subset = ["nl_tags"], inplace=True)
    return data
