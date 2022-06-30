from rest_framework import serializers
from api.models.author import Author
from django.db import transaction
from django.contrib.auth.models import User

class AuthorSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.CharField(source='user.email')
    password = serializers.CharField(source='user.password') # This field is not shown to users

    class Meta:
        model = Author
        fields = ['id', 'username', 'first_name', 'last_name', 'bio', 'email', 'password']

    @transaction.atomic
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        if User.objects.filter(username=user_data['username']).count() > 0:
            raise serializers.ValidationError({'user':'User with this username already exists'})
        user = User(username=user_data['username'], 
                                   email=user_data['email'], 
                                   first_name=user_data['first_name'],
                                   last_name=user_data['last_name'])
        user.set_password(user_data['password'])
        user.save()
        validated_data['user'] = user
        return super().create(validated_data)
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop('password')
        return data