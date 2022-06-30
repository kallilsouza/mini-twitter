from rest_framework import status, viewsets
from api.models.post import Post
import django_filters
from api.serializers.post import PostSerializer
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q

def only_following(queryset, filter, field):
    return queryset

class PostFilter(django_filters.FilterSet):
    only_following = django_filters.BooleanFilter(method=only_following, label='only_following')

    class Meta:
        model = Post
        fields = ['only_following', 'author']

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = PostFilter
    search_fields = ['text']

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.GET.get('author', None) == str(self.request.user.author.id):
            queryset = queryset.filter(~Q(author=self.request.user.author))        
        only_following = True if self.request.GET.get('only_following', 'false').lower() == 'true' else False
        if only_following == True:
            queryset = queryset.filter(author__followers=self.request.user.author)
        return queryset

    http_method_names = ['get', 'post']