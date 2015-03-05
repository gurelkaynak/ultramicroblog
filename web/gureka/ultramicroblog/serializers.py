from django.forms import widgets
from rest_framework import serializers
from .models import Post 

class PostSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Post 
        fields = ('id', 'title', 'text', 'created_date')
