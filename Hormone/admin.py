# Hormone/admin.py

# Import modules/packages
from django.contrib import admin
from .models import (
    Hormone, 
    HormoneUser, HormoneProducer, 
    Order, Promotion, RenewableEnergyType, SellerRating
)

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
    list_display = ('user', 'get_type_of_energy', 'get_rating')

    def get_type_of_energy(self, obj):
        # Implement logic to get type_of_energy based on the related models
        return ", ".join([energy.get_ingins_type for energy in obj.renewableenergytype_set.all()])
    
    get_type_of_energy.short_description = 'Top Ingins'



    def get_rating(self, obj):
        # Implement logic to get rating based on the related models
        # For example, you may want to calculate an average rating
        return 0.0  # Replace with your logic
    
    get_rating.short_description = 'Rating'



# Customize the display of HormoneProducer in the admin interface
class HormoneProducerAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_storefront', 'get_ingins_type', 'get_storage', 'get_total_sales', 'get_trends')

    def get_storefront(self, obj):
        # Implement the logic to get storefront information/ 
        # information about all what the seller is selling to showcase to the buyer
        storefronts = [hormone.description for hormone in obj.hormone_set.all()]
        return ', '.join(storefronts)

    def get_ingins_type(self, obj):
        # Implement the logic to get engine type information
        # Assuming 'renewableenergytype' is a ForeignKey in HormoneProducer pointing to RenewableEnergyType
        ingins_type = obj.renewableenergytype.engine_type if obj.renewableenergytype else None
        return ingins_type
    
    def get_storage(self, obj):
        # Implement the logic to get storage information
       orders = obj.order_set.all()  # Assuming the related name is 'order_set'
       storage_info = ', '.join([order.storage for order in orders if order.storage])
       return storage_info

    def get_total_sales(self, obj):
        # Implement the logic to get total sales information
        total_sales = sum(order.sales for order in obj.order_set.all())
        return obj.total_sales
    

    def get_trends(self, obj):
        # Implement the logic to get trends information
        promotions = Promotion.objects.filter(HormoneProducer=obj)
        top_renewable_types = RenewableEnergyType.objects.filter(HormoneProducer=obj).order_by('-sales')[:5]

        trends_info = {
            'promotions': [promotion.details for promotion in promotions],
            'top_renewable_types': [renewable_type.get_ingins_type for renewable_type in top_renewable_types],
        }

        return trends_info



# Manage and view 'HormoneUser' objects through the admin interface with custom display.
admin.site.register(Hormone, HormoneAdmin)

# Manage and view 'HormoneUser' objects through the admin interface with custom display.
admin.site.register(HormoneUser, HormoneUserAdmin)

# Manage and view 'HormoneProducer' objects through the admin interface with custom display.
admin.site.register(HormoneProducer, HormoneProducerAdmin)
admin.site.register(SellerRating)


