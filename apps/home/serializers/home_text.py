from rest_framework import serializers
from apps.home.models import HomeText


class HomeTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeText
        fields = ['title', 'main_text', 'secondary_text']
