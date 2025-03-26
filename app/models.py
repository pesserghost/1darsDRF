from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator
from rest_framework import serializers, viewsets, routers
from django.contrib import admin
from django.utils.timezone import now
from django.urls import path, include

# 1. Category Model
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

admin.site.register(Category)

# 2. Article Model
class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_at = models.DateTimeField(default=now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles')
    views = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title

admin.site.register(Article)

# 3. Comment Model
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user_name = models.CharField(max_length=255)
    email = models.EmailField()
    text = models.TextField()
    published_at = models.DateTimeField(default=now)

    def __str__(self):
        return f'Comment by {self.user_name} on {self.article.title}'

admin.site.register(Comment)
