from rest_framework import status, viewsets
from api.models.author import Author
from api.serializers.author import AuthorSerializer
import django_filters
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework.decorators import action, authentication_classes
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    http_method_names = ['get', 'post']    

    @action(methods=['POST'], name='Follow users', detail=True)    
    def follow(self, request, *args, **kwargs):
        author = get_object_or_404(Author, pk=kwargs['pk'])  
        if author == self.author:
            return HttpResponse(status=403)
        author.add_to_followers(request.user.author)
        return HttpResponse(status=200)

    @action(methods=['POST'], name='Unfollow users', detail=True)    
    def unfollow(self, request, *args, **kwargs):
        author = get_object_or_404(Author, pk=kwargs['pk'])  
        author.remove_from_followers(request.user.author)
        return HttpResponse(status=200)

    @authentication_classes([])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def get_permissions(self):        
        if self.request.method == 'POST':
            permissions = []
        else:
            permissions = super().get_permissions()
        return permissions