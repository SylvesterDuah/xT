# **Documentation**
#  Defining serializers for the Django models (Extend, Overdrive, and Hormone) using Django REST Framework's ModelSerializer. 
# Additionally, creating serializers for the forms (ExtendForm, OverdriveForm, and HormoneForm).
# This part defines the serializers for the Django models (Extend, Overdrive, and Hormone), 
# which will be used in converting instances of these models to and from JSON when working with Django REST Framework.

# Overdrive/ serializers.py


# Import modules and classes
from rest_framework.serializers import ModelSerializer
from .models import Overdrive, OverdriveUser, OverdriveProducer
from .forms import OverdriveUserForm, OverdriveProducerForm
# Define a serializer for the Extend model



# Define a serializer for the Overdrive model

class OverdriveSerializer(ModelSerializer):
    class Meta:
        model= Overdrive
        fields = '__all__'




class OverdriveUserSerializer(ModelSerializer):
    class Meta:
        # Specify the model for which the serializer is created
        model = OverdriveUser
        # Include all fields from the model in the serializer
        fields = '__all__'



# Forms.py for overdrive
# Define serializer for the OverdriveFormSerializer form
class OverdriveUserFormSerializer(ModelSerializer):
    class Meta:
        # Specify the model for which the serializer is created
        model = OverdriveUserForm
        # Include all fields from the form in the serializer
        fields = '__all__'




# serializers.py
class OverdriveProducerSerializer(ModelSerializer):
    class Meta:
        model = OverdriveProducer
        fields = '__all__'




class OverdriveProducerFormSerializer(ModelSerializer):
    class Meta:
        # Specify the model for which the serializer is created
        model = OverdriveProducerForm
        # Include all fields from the form in the serializer
        fields = '__all__'


