from rest_framework import serializers
from .models import Proprosal


class ProprosalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proprosal
        fields = ['id', 'title']


class ProprosalCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proprosal
        fields = ['title', 'description']



class ProprosalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proprosal
        fields = ['id', 'title', 'description', 'photo']
