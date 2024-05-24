from rest_framework import serializers
from app.models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = ['id', 'name']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'category', 'image', 'description', 'url']

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'name', 'part', 'body', 'created_at', 'slug', 'photo']