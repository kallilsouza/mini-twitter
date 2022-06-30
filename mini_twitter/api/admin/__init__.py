from django.contrib import admin
from api.models import Author, Post
from .author import AuthorAdmin
from .post import PostAdmin

admin.site.site_header = 'Mini-Twitter'
admin.site.site_title = 'Mini-Twitter'

admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)