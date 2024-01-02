# **Documentation**
#  Defining serializers for the Django models (Extend, Overdrive, and Hormone) using Django REST Framework's ModelSerializer. 
# Additionally, creating serializers for the forms (ExtendForm, OverdriveForm, and HormoneForm).
# This part defines the serializers for the Django models (Extend, Overdrive, and Hormone), 
# which will be used in converting instances of these models to and from JSON when working with Django REST Framework.


# Import modules and classes
from rest_framework.serializers import ModelSerializer
from .models import Extend, Overdrive, Hormone
from .forms import ExtendForm, OverdriveForm, HormoneForm

# Define a serializer for the Extend model
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


# Define a serializer for the Overdrive model
class OverdriveSerializer(ModelSerializer):
    class Meta:
        # Specify the model for which the serializer is created
        model = Overdrive
        # Include all fields from the model in the serializer
        fields = '__all__'

# Forms.py for overdrive
# Define serializer for the OverdriveFormSerializer form
class OverdriveFormSerializer(ModelSerializer):
    class Meta:
        # Specify the model for which the serializer is created
        model = OverdriveForm
        # Include all fields from the form in the serializer
        fields = '__all__'


# Define a serializer for the Hormone model
class HormoneSerializer(ModelSerializer):
    class Meta:
        # Specify the model for which the serializer is created
        model = Hormone
        # Include all fields from the model in the serializer
        fields = '__all__'

# Forms.py for Hormone
# Define a serializer for the HormoneFormSerializer form
class HormoneFormSerializer(ModelSerializer):
    class Meta:
        # Specify the model for which the serializer is created
        model = HormoneForm
        # Include all fields from the form in the serializer
        fields = '__all__'
