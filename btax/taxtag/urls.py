from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from taxtag.views import ArticleListView,TagListView



urlpatterns = [

    path('', ArticleListView.as_view(), name='home'),
    path('tags/', TagListView.as_view(), name='tag_list'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)