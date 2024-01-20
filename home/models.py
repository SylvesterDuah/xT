# Home/models.py


# Import modules/packages
from django.db import models


from django.contrib.auth.models import User
from accounts.serializers import SellerRegistrationSerializer



from django.utils import timezone
from .Components.carousel import Carousel




# The main app
# This is a model called 'Extend' that represents the home/landing page of the app.
# It has three main attributes: 'name/ingin', 'source', and 'hot_prices'.
class Extend(models.Model):

   
    # 'name' is a short text describing this thing, like a product name.
    name = models.CharField(max_length=100)
    SOLAR = "SOLAR"
    WIND = "WIND"
    HYDRO = "HYDRO"
    GEOTHERMAL = "GEOTHERMAL"
    BIOGAS = "BIO-GAS"
    BIOFUEL = "BIO-FUEL"
    source_choices = [
        (SOLAR, 'Solar'),
        (WIND, 'Wind'),
        (HYDRO, 'Hydro'),
        (GEOTHERMAL, 'Geothermal'),
        (BIOGAS, 'Bio-gas'),
        (BIOFUEL, 'Bio-fuel')
    ]

     # 'source' is a dropdown choice field for the energy source (like solar or wind).
    source = models.CharField(max_length=50, choices=source_choices, default=SOLAR,)

    # 'hot_prices' is a number field representing the cost of the current energy. 
    # It has to be changing every second like crytocurrency prices
    hot_prices = models.DecimalField(max_digits=5, decimal_places=2)

    
    

    # Refer to this object, to show its 'name'.
    def __str__(self):
        return self.name
    

    # Query to sort based on their 'hot_prices'.
    class Meta:
        ordering = ['hot_prices']



    @property
    def get_ingins(self):
        # Retrieve top ingredients sorted by ratings
        return self.ingins.order_by('-rating')


    # Carousel Feteching from Carousel.py
    def get_carousel_news(self):
        # Create a Carousel instance with user location
        carousel = Carousel(user_location='CurrentLocation')

        # Fetch news using the Carousel instance
        news_items = carousel.fetch_news()

        return news_items
