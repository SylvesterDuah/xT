
# home/forms.py
from django import forms

from .models import OverdriveUser, OverdriveProducer


class OverdriveUserForm(forms.ModelForm):
    class Meta:
        model = OverdriveUser
        fields = '__all__'



class OverdriveProducerForm(forms.ModelForm):
    class Meta:
        model = OverdriveProducer
        fields = '__all__'
