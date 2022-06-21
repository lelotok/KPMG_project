from django.shortcuts import render
import datetime
import pandas as pd
import numpy as np

from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from taxtag.models import Article,Tag


from taxtag.scrape import get_res,get_numac_numbers,scrape_numac,create_numac_links,clean
from taxtag.summary import summarise,tagging,create_tags,clean_dataframe




class ArticleListView(ListView):
    model = Article
    ordering = ['date' , 'numac']

class TagListView(ListView):
    model = Tag
    ordering = ['tag' , 'level']



def tagsearch(request,tag):
    '''
    Function to bring selected articles
    '''
    articles=Article.objects.filter(nl_tags__icontains=tag)

    context = {'data':{'articles': articles}}
    return render(request, 'home.html', context)
    

def home(request):
    '''
    Root page of the app
    '''
    articles=Article.objects.all() 
    context = {'data':{'articles': articles}}
    return render(request, 'home.html', context)



def tagone(request):
    '''
    Function to tag a given article text 
    '''
    
    template_name = './taxtag/tagone.html'
    if request.method == 'POST':

        text=[]
        
        _q=request.POST.get("all_article")
        rettext=_q
        _q=clean(_q)
        _q=_q.replace('\n',"")
        text.append(_q)
        summary=summarise(text)
        nltags=create_tags(summary)
        print(summary, nltags)
        
        context=summary[0]
        
        context = {'summary': summary[0],'tags':nltags[0],'text':rettext}


        return render(request, template_name, context)
    return render(request, template_name, {'form': 0})
  


def savearticles(request):
    '''
    Function to scrape given date and tag tax related articles and save to database
    '''
    DATE='2022-06-15'

    res = get_res(DATE)
    numacs=get_numac_numbers(res.text)
    numac_links=create_numac_links(numacs,DATE)
    nl_list=scrape_numac(numac_links)

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

    for index, row in data.iterrows():
        x=Article()
        x.date=row['date']
        x.numac=row['numac']
        x.link=row['link']
        x.nl_text=row['nl_text']
        x.nl_sum=row['nl_sum']
        x.nl_tags=row['nl_tags']
        x.save()
    
    
    articles=Article.objects.all() 
       
    context = {'data':{'articles': articles}}
    return render(request,'home.html',context)
