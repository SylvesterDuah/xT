# Overdrive/serializers.py

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Overdrive, OverdriveUser, OverdriveProducer
from .forms import OverdriveUserForm, OverdriveProducerForm

# Define a serializer for the Extend model

# Define a serializer for the Overdrive model
class OverdriveSerializer(ModelSerializer):
    energy_forecast_news = serializers.CharField()
    class Meta:
        model = Overdrive
        fields = '__all__'

# Define a serializer for the OverdriveUser model
class OverdriveUserSerializer(ModelSerializer):
    energy_forecast_news = serializers.CharField()
    class Meta:
        model = OverdriveUser
        fields = '__all__'

# Define serializer for the OverdriveUserForm form
class OverdriveUserFormSerializer(ModelSerializer):
    energy_forecast_news = serializers.CharField()
    class Meta:
        model = OverdriveUser  # Use the corresponding model
        fields = '__all__'

# Define serializer for the OverdriveProducer model
class OverdriveProducerSerializer(ModelSerializer):
    energy_forecast_news = serializers.CharField()
    class Meta:
        model = OverdriveProducer
        fields = '__all__'

# Define serializer for the OverdriveProducerForm form
class OverdriveProducerFormSerializer(ModelSerializer):
    energy_forecast_news = serializers.CharField()
    class Meta:
        model = OverdriveProducer  # Use the corresponding model
        fields = '__all__'
