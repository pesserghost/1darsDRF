from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Article, Comment

admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Comment)
