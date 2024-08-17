from rest_framework import serializers
from .models import *

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'
        
class CardFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card_Front
        fields = '__all__'
        
class CardBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card_Back
        fields = '__all__'