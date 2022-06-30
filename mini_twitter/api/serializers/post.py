from rest_framework import serializers
from api.models.post import Post
from api.serializers.author import AuthorSerializer

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(required=False)

    class Meta:
        model = Post
        fields = ['id', 'author', 'text']

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user.author
        return super().create(validated_data)