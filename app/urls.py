
from django.urls import path

from .views import ArticleApi, ArticleDetailApi, CategoryApi, CategoryDetailApi

urlpatterns = [
    path('category/', CategoryApi.as_view()),
    path('category/<int:pk>/', CategoryDetailApi.as_view()),

    path('article/', ArticleApi.as_view()),
    path('article/<int:pk>/', ArticleDetailApi.as_view()),
]
