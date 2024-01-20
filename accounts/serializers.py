# accounts/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import SellerRegistration

# class BuyerRegistrationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = [
#             'username', 
#             'password', 
#             'email', 
#             'first_name', 
#             'last_name', 
#             'phone_number', 
#             'country', 
#             'state', 
#             'city', 
#             'zipcode'
#         ]




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

class SellerRegistrationSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = SellerRegistration
        fields = ['user', 'company_name', 'company_email', 'energy_source', 'phone_number', 'country', 'state', 'city', 'zipcode']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        seller = SellerRegistration.objects.create(user=user, **validated_data)
        return seller



# class SellerRegistrationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'password',
#             'email',
#             'company_name',
#             'energy_source',
#             'phone_number',
#             'country',
#             'state',
#             'city',
#             'zipcode'
#         ]

#     def create(self, validated_data):
#         energy_source = validated_data.pop('energy_source', None)
#         user = User.objects.create(**validated_data)
#         UserProfile.objects.create(
#             user=user,
#             company_name=validated_data['company_name'],
#             energy_source=energy_source,
#             phone_number=validated_data['phone_number'],
#             country=validated_data['country'],
#             state=validated_data['state'],
#             city=validated_data['city'],
#             zipcode=validated_data['zipcode']
#         )
#         return user

# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = '__all__'



# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'

# class UserRegistrationSerializer(serializers.ModelSerializer):
#     energy_source = serializers.ChoiceField(choices=User.ENERGY_SOURCE_CHOICES, required=False)

#     class Meta:
#         model = User
#         fields = '__all__'


 
        
