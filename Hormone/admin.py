# Hormone/admin.py

# Import modules/packages
from django.contrib import admin
from .models import  Hormone, HormoneUser, HormoneProducer

# Customize the display of HormoneUser in the admin interface

class HormoneAdmin(admin.ModelAdmin):
    list_display = (
        "description",
        "hormone_image",
        "models_and_specifications",
        "key_benefits",
        "getting_started_guide",
        "renewable_energy_stores",
        "pricing_information",
        "sustainability_commitment",
        "login_signup_prompt",
    )


class HormoneUserAdmin(admin.ModelAdmin):
    # Customize the list display as needed
    list_display = ('name', 'type_of_energy', 'rating',)

# Customize the display of HormoneProducer in the admin interface
class HormoneProducerAdmin(admin.ModelAdmin):
    # Customize the list display as needed
    list_display = ('user_profile', 'storefront', 'engine_type', 'storage', 'total_sales',)



# Manage and view 'HormoneUser' objects through the admin interface with custom display.
admin.site.register(Hormone, HormoneAdmin)

# Manage and view 'HormoneUser' objects through the admin interface with custom display.
admin.site.register(HormoneUser, HormoneUserAdmin)

# Manage and view 'HormoneProducer' objects through the admin interface with custom display.
admin.site.register(HormoneProducer, HormoneProducerAdmin)


