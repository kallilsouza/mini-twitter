from rest_framework import status, viewsets
from api.models.author import Author
from api.serializers.author import AuthorSerializer
import django_filters
from django_filters.rest_framework.backends import DjangoFilterBackend

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    http_method_names = ['get', 'post']

    def get_authenticators(self):        
        if self.request.method == 'POST':
            authenticators = []
        else:
            authenticators = super().get_authenticators()
        return authenticators

    def get_permissions(self):
        if self.request.method == 'POST':
            permissions = []
        else:
            permissions = super().get_permissions()
        return permissions