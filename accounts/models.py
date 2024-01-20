# accounts/models.py

from django.db import models
from django.contrib.auth.models import User

class SellerRegistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # password = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    company_email = models.EmailField(unique=True)
    energy_source = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        return self.company_name


# class User(AbstractUser):
#     email = models.EmailField(unique=True)
#     company_name = models.CharField(max_length=100, blank=True, null=True)
#     phone_number = models.CharField(max_length=10, blank=True, null=True)
#     country = models.CharField(max_length=50, blank=True, null=True)
#     state = models.CharField(max_length=50, blank=True, null=True)
#     city = models.CharField(max_length=50, blank=True, null=True)
#     zipcode = models.CharField(max_length=5, blank=True, null=True)

#     SOLAR = "SOLAR"
#     WIND = "WIND"
#     HYDRO = "HYDRO"
#     GEOTHERMAL = "GEOTHERMAL"
#     BIOGAS = "BIO-GAS"
#     BIOFUEL = "BIO-FUEL"

#     ENERGY_SOURCE_CHOICES = [
#         (SOLAR, 'Solar'),
#         (WIND, 'Wind'),
#         (HYDRO, 'Hydro'),
#         (GEOTHERMAL, 'Geothermal'),
#         (BIOGAS, 'Bio-gas'),
#         (BIOFUEL, 'Bio-fuel')
#     ]


    

   


#     email = models.EmailField(unique=True)
#     phone_number = models.CharField(max_length=10)
#     company_name = models.CharField(max_length=100)
#     energy_source = ArrayField(models.CharField(
#         max_length=20, choices=ENERGY_SOURCE_CHOICES, 
#         blank=True, null=True), blank=True, null=True)
#     country = models.CharField(max_length=50)
#     state = models.CharField(max_length=50)
#     city = models.CharField(max_length=50)
#     zipcode = models.CharField(max_length=5)

#     # Add related_name to avoid clashes with auth.User
#     groups = models.ManyToManyField(
#         "auth.Group",
#         related_name="user_accounts",
#         related_query_name="user_account",
#         blank=True,
#         help_text="The groups this user belongs to.",
#     )
#     user_permissions = models.ManyToManyField(
#         "auth.Permission",
#         related_name="user_accounts",
#         related_query_name="user_account",
#         blank=True,
#         help_text="Specific permissions for this user.",
#     )




# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     is_buyer = models.BooleanField(default=False)
#     is_seller = models.BooleanField(default=False)

#     # Import ENERGY_SOURCE_CHOICES from the User model
#     ENERGY_SOURCE_CHOICES = User.ENERGY_SOURCE_CHOICES

#     # Add these fields to store additional information
#     company_name = models.CharField(max_length=100, blank=True, null=True)
#     energy_source = ArrayField(
#         models.CharField(max_length=20, choices=ENERGY_SOURCE_CHOICES, blank=True, null=True),
#         blank=True,
#         null=True,
#     )

#     phone_number = models.CharField(max_length=10, blank=True, null=True)
#     country = models.CharField(max_length=50, blank=True, null=True)
#     state = models.CharField(max_length=50, blank=True, null=True)
#     city = models.CharField(max_length=50, blank=True, null=True)
#     zipcode = models.CharField(max_length=5, blank=True, null=True)

#     def __str__(self):
#         return self.user.username
    






