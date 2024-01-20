# Overdrive/admin.py

# Import modules/packages
from django.contrib import admin
from .models import Overdrive, OverdriveUser, OverdriveProducer



# Customize the display of OverdriveUser in the admin interface

class OverdriveAdmin(admin.ModelAdmin):
    list_display = (
        'description', 
        'overdrive_image', 
        'models_and_specifications', 
        'key_benefits',
        'getting_started_guide',
        'pricing_information',
        'customer_testimonials',
        'sustainability_commitment',
    )



class OverdriveUserAdmin(admin.ModelAdmin):
    list_display = ('capacity', 'charging_speed', 'energy_forecast_news_feature', 'energy_forecast_news')

# Customize the display of OverdriveProducer in the admin interface
class OverdriveProducerAdmin(admin.ModelAdmin):
    # Customize the list display as needed
    list_display = ('capacity', 'charging_speed')


# Manage and view 'Overdrive' objects through the admin interface with custom display.
admin.site.register(Overdrive, OverdriveAdmin)

# Manage and view 'OverdriveUser' objects through the admin interface with custom display.
admin.site.register(OverdriveUser, OverdriveUserAdmin)

# Manage and view 'OverdriveProducer' objects through the admin interface with custom display.
admin.site.register(OverdriveProducer, OverdriveProducerAdmin)