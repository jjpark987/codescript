from rest_framework import serializers
from .models import Response

class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = ['id', 'title', 'analysis', 'score', 'created_at', 'submission']
        extra_kwargs = {
            'submission': {'read_only': True},
        }