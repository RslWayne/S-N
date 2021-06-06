import profile

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .models import Profile
from .views import *

urlpatterns = [
    path('', news_page, name='news'),
    path('art/',article_page),
    path('news/<int:news_id>',news_detail,name='news_detail'),
    path('like/<int:news_id>/',like,name='like'),
    path('dislike/<int:news_id>/',dislike,name='dislike'),
    path('profile/',profile_settings,name='profile')

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
