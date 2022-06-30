from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import AuthorViewSet

author_router = DefaultRouter()
author_router.register('authors', AuthorViewSet, basename='authors')