# Home/admin.py

# Import modules/packages
from django.contrib import admin
from .models import Extend

# Manage and view 'Extend' objects through the admin interface.
admin.site.register(Extend)
