from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register([News,Like,Comment,Image,Dislike,Profile,Post])

