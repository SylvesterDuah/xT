# account/forms/py

from django.contrib.auth.forms import UserChangeForm
from .models import SellerRegistration

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = SellerRegistration
        fields = ('user', 'company_email', 'energy_source', 'phone_number', 'country', 'state', 'city', 'zipcode')


