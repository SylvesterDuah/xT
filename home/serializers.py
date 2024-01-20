# **Documentation**
#  Defining serializers for the Django models (Extend, Overdrive, and Hormone) using Django REST Framework's ModelSerializer. 
# Additionally, creating serializers for the forms (ExtendForm, OverdriveForm, and HormoneForm).
# This part defines the serializers for the Django models (Extend, Overdrive, and Hormone), 
# which will be used in converting instances of these models to and from JSON when working with Django REST Framework.

# Home/ serializers.py


# Import modules and classes
from rest_framework.serializers import ModelSerializer
from .models import Extend
from .forms import ExtendForm, SellerRegistrationSerializerForm
# Define a serializer for the Extend model

# serializers.py
from rest_framework import serializers

class ChoiceSerializer(serializers.Serializer):
    registration_choices = serializers.ListField()
    login_choices = serializers.ListField()

class ExtendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extend
        fields = ['name', 'source', 'hot_prices']



class ExtendSerializer(ModelSerializer):
    class Meta:
        # Model for the serializer 
        model = Extend
        # Include all fields from the model in the serializer
        fields = '__all__'


# Forms.py for overdrive
# Define a serializer for the ExtendFormSerializer form 
class ExtendFormSerializer(ModelSerializer):
    class Meta:
        # Specify the model for which the serializer is created
        model = ExtendForm
        # Include all fields from the form in the serializer
        fields = '__all__'




