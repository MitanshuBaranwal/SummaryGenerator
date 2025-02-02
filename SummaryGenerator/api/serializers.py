from rest_framework import serializers
from .models import TextData

class TextDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextData
        fields = ['id', 'original_text', 'summary', 'bullet_points', 'created_at']