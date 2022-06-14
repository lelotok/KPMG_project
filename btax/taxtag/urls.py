from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from taxtag.views import ArticleListView,TagListView,home,savearticles,tagone,tagsearch



urlpatterns = [

    
    path('', home, name='home'),
    path('tags/', TagListView.as_view(), name='tag_list'),
    path('', ArticleListView.as_view(), name='article_list'),
    path('save', savearticles, name='save_articles'),
    path('tagone',tagone, name='tagone'),
    path('tags/<str:tag>/',tagsearch, name='tagsearch'),

    




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)