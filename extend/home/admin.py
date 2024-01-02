# Import modules/packages
from django.contrib import admin
from .models import Extend, Overdrive, Hormone






# Manage and view 'Extend' objects through the admin interface.
admin.site.register(Extend)

# Manage and view 'Overdrive' objects through the admin interface.
admin.site.register(Overdrive)

# Manage and view 'Hormone' objects through the admin interface.
admin.site.register(Hormone)


