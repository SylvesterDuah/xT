from rest_framework.serializers import ModelSerializer
from .models import Extend, Overdrive, Hormone
from .forms import ExtendForm, OverdriveForm, HormoneForm



class ExtendSerializer(ModelSerializer):
    class Meta:
        model = Extend
        fields = '__all__'


# Forms.py for overdrive
class ExtendFormSerializer(ModelSerializer):
    class Meta:
        model = ExtendForm
        fields = '__all__'








class OverdriveSerializer(ModelSerializer):
    class Meta:
        model = Overdrive
        fields = '__all__'

# Forms.py for overdrive
class OverdriveFormSerializer(ModelSerializer):
    class Meta:
        model = OverdriveForm
        fields = '__all__'








class HormoneSerializer(ModelSerializer):
    class Meta:
        model = Hormone
        fields = '__all__'


# Forms.py for Hormone
class HormoneFormSerializer(ModelSerializer):
    class Meta:
        model = HormoneForm
        fields = '__all__'

