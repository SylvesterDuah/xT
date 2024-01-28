# Homrmone/models.py
from django.db import models
from django.contrib.auth.models import User
from home.Components.carousel import Carousel



# Ecommerce
# 'Hormone' representing as an ecommerce system.
# Features for Ecommerce Main Page (Without Login)
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




from django.db import models
from django.contrib.auth.models import User

class HormoneUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add other HormoneUser-related fields if needed

    def get_renewable_energy_types(self):
        """
        Get all renewable energy types associated with the user's sellers.
        """
        sellers = HormoneProducer.objects.filter(user=self.user)
        ingins_types = RenewableEnergyType.objects.filter(HormoneProducer__in=sellers)
        return ingins_types

    def get_top_ingins(self):
        """
        Get the top renewable energy types based on the highest-rated sellers.
        Returns a list of dictionaries with seller information and ratings.
        """
        sellers = HormoneProducer.objects.filter(user=self.user)
        top_ingins = []

        for seller in sellers:
            ratings = SellerRating.objects.filter(seller=seller).order_by('-rating')
            if ratings.exists():
                top_ingin = {
                    'company_name': seller.user.username,
                    'ingins_type': seller.renewableenergytype.get_ingins_type,
                    'rating': ratings.first().rating,
                }
                top_ingins.append(top_ingin)

        top_ingins.sort(key=lambda x: x['rating'], reverse=True)
        return top_ingins




    
    



# Represents products in the ecommerce system

class HormoneProducer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Other HormoneProducer-related fields

class SellerRating(models.Model):
    seller = models.ForeignKey(HormoneProducer, on_delete=models.CASCADE)
    rating = models.FloatField()

class Product(models.Model):
    HormoneProducer = models.ForeignKey(HormoneProducer, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    # Other product-related fields

class RenewableEnergyType(models.Model):
    HormoneProducer = models.ForeignKey(HormoneProducer, on_delete=models.CASCADE)
    get_ingins_type = models.CharField(max_length=255)
    # Other renewable energy type-related fields

class Order(models.Model):
    HormoneProducer = models.ForeignKey(HormoneProducer, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    # Other order-related fields

class Promotion(models.Model):
    HormoneProducer = models.ForeignKey(HormoneProducer, on_delete=models.CASCADE)
    details = models.TextField()
    # Other promotion-related fields

# Define other models for customer orders, management, integration, total sales, total tenure, reports, etc.

class ContributionToEcosystem(models.Model):
    HormoneProducer = models.ForeignKey(HormoneProducer, on_delete=models.CASCADE)
    project_details = models.TextField()
    # Other contribution-related fields

class Analytics(models.Model):
    HormoneProducer = models.ForeignKey(HormoneProducer, on_delete=models.CASCADE)
    predictions = models.TextField()
    # Other analytics-related fields

