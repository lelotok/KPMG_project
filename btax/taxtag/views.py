from django.shortcuts import render

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from taxtag.models import Article,Tag

# Create your views here.
class ArticleListView(ListView):
    model = Article
    ordering = ['date' , 'numac']



class TagListView(ListView):
    model = Tag
    ordering = ['tag' , 'level']