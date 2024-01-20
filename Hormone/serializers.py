# Home/ serializers.py


# Import modules and classes
from rest_framework.serializers import ModelSerializer
from .models import Hormone, HormoneUser, HormoneProducer

# serializers.py
from rest_framework import serializers


# Define a serializer for the Hormone model
class HormoneSerializer(ModelSerializer):
    class Meta:
        model = Hormone
        fields = '__all__'




class HormoneUserSerializer(ModelSerializer):
    class Meta:
        # Specify the model for which the serializer is created
        model = HormoneUser
        # Include all fields from the model in the serializer
        fields = '__all__'



class HormoneProducerSerializer(ModelSerializer):
    class Meta:
        # Specify the model for which the serializer is created
        model = HormoneProducer
        # Include all fields from the model in the serializer
        fields = '__all__'


