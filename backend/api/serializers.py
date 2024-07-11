from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Subcategory, Problem, Submission

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['id', 'name', 'description', 'category']
        extra_kwargs = {
            'category': {'read_only': True},
        }

class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ['id', 'title', 'description', 'examples', 'example_images', 'constraints', 'difficulty', 'created_at', 'updated_at', 'category', 'subcategory']
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'category': {'read_only': True},
            'subcategory': {'read_only': True},
        }

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['id', 'content', 'created_at', 'updated_at', 'problem', 'user']
        extra_kwargs = {
            'created_at': {'read_only': True},
            'problem': {'read_only': True},
            'user': {'read_only': True},
        }
