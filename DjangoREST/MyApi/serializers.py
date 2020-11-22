from rest_framework import serializers
from MyApi.models import itellyou, LANGUAGE_CHOICES, STYLE_CHOICES

class itellyouSerializer(serializers.ModelSerializer):
    class Meta:
        model = itellyou
        fields = ('id', 'key', 'name')