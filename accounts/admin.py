from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm  
from .models import SellerRegistration, User

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(SellerRegistration)
