# Homrmone/models.py
from django.db import models
from django.contrib.auth.models import User
from home.Components.carousel import Carousel



# Ecommerce
# 'Hormone' representing as an ecommerce system.
# Features for Powerwall Main Page (Without Login)
class Hormone(models.Model):
    
    # Display general information about Powerwall
    description = models.TextField(blank=True, null=True)

    # Image field for adding a main page image
    hormone_image = models.ImageField(upload_to='hormone/', null=True, blank=True)
    
    
    
    # Display available models and their specifications
    models_and_specifications = models.TextField(blank=True, null=True)
    
    # Highlight key benefits of using Powerwall
    key_benefits = models.TextField(blank=True, null=True)
    
    # Provide information on how to get started with Powerwall
    getting_started_guide = models.TextField(blank=True, null=True)

    # Field for renewable energy stores
    renewable_energy_stores = models.TextField(blank=True, null=True)
    
    # Display pricing information or link to pricing details
    pricing_information = models.TextField(blank=True, null=True)
    

    # Display information about Overdrive's commitment to sustainability
    sustainability_commitment = models.TextField(blank=True, null=True)
    
    # Include a call-to-action for users to log in or sign up
    login_signup_prompt = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return "Hormone"





class HormoneUser(models.Model):
    name = models.CharField(max_length=100, default="")
    type_of_energy = models.CharField(max_length=100, default="")
    rating = models.FloatField(default=0.0)
    source = models.CharField(max_length=20, choices=[], blank=True)


    # Field for deals of the week
    deals_of_the_week = models.JSONField(blank=True, null=True)

    source_choices = [
        ('Solar', 'Solar'),
        ('wind', 'Wind'),
    ]

    def __str__(self):
        return self.name
    

    

    @property
    def get_top_ingins(self):
        # Retrieve top ingredients sorted by ratings
        return self.top_ingins.order_by('-rating')

    def save(self, *args, **kwargs):
        # Set choices dynamically from SellerRegistrationSerializer
        # seller_serializer = SellerRegistrationSerializer()
        # self.source = models.CharField(max_length=20, choices=seller_serializer.fields['energy_source'].choices, blank=True)
        super().save(*args, **kwargs)


    
    



# Represents products in the ecommerce system
class HormoneProducer(models.Model):
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE)
    storefront = models.CharField(max_length=100, default="")
    engine_type = models.CharField(max_length=100, default="")
    storage = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    promotions = models.TextField(blank=True)
    customer_orders = models.PositiveIntegerField(default=0)
    management = models.TextField(blank=True)
    integration = models.TextField(blank=True)
    total_sales = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total_tenure = models.PositiveIntegerField(default=0)
    reports = models.TextField(blank=True)
    contributions_to_ecosystem = models.TextField(blank=True)
    analytics = models.TextField(blank=True)

    def __str__(self):
        return self.user_profile.username
