
from django.contrib.auth.models import User
from django.forms import model_to_dict
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article, Category


# Create your views here.

class CategoryApi(APIView):
    def get(self, request):
        category = Category.objects.all()
        a = []
        for i in category:
            a.append(model_to_dict(i))
        return Response(a)

    def post(self, request):
        category = Category.objects.create(
            name= request.data["name"]
        )
        return Response(model_to_dict(category))

class CategoryDetailApi(APIView):
    def get(self, request, pk):
        article = Category.objects.get(pk=pk)
        return Response(model_to_dict(article))


class ArticleApi(APIView):
    def get(self, request):
        article = Article.objects.all()
        a = []
        for i in article:
            a.append(model_to_dict(i))
        return Response(a)

    def post(self, request):
        category = get_object_or_404(Category, id=request.data['category'])
        author = get_object_or_404(User, id=request.data['author'])
        article = Article.objects.create(
            title=request.data['title'],
            description=request.data['description'],
            category=category,
            author=author,
        )
        return Response(model_to_dict(article))

class ArticleDetailApi(APIView):
    def get(self, request, pk):
        article = Article.objects.get(pk=pk)
        return Response(model_to_dict(article))
