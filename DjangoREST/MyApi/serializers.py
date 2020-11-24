from rest_framework import serializers
from MyApi.models import itellyou,itellyou_detali,itellyou_lang_edition,itellyou_software_message, LANGUAGE_CHOICES, STYLE_CHOICES

# 我告诉你基础序列化
class itellyouSerializer(serializers.ModelSerializer):
    class Meta:
        model = itellyou
        fields = ('id', 'key', 'name')
# 我告诉你明细序列化
class itellyou_detaliSerializer(serializers.ModelSerializer):
    class Meta:
        model = itellyou_detali
        fields = ('id', 'father_key','key', 'name')

#  我告诉你语言版本
class itellyou_lang_editionSerializer(serializers.ModelSerializer):
    class Meta:
        model = itellyou_lang_edition
        fields = ('id', 'father_key','key', 'lang')


# 我告诉你最终软件版本信息
class itellyou_software_messageSerializer(serializers.ModelSerializer):
    class Meta:
        model = itellyou_software_message
        fields = ('id', 'father_key','key', 'name','edition_date','download_url')