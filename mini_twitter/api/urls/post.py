from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import PostViewSet

post_router = DefaultRouter()
post_router.register('posts', PostViewSet, basename='post')