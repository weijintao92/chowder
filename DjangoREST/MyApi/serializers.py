from rest_framework import serializers
from MyApi.models import itellyou, LANGUAGE_CHOICES, STYLE_CHOICES

# 我告诉你基础序列化
class itellyouSerializer(serializers.ModelSerializer):
    class Meta:
        model = itellyou
        fields = ('id', 'key', 'name')
# 我告诉你明细序列化
class itellyou_detaliSerializer(serializers.ModelSerializer):
    class Meta:
        model = itellyou
        fields = ('id', 'father_key','key', 'name')