# **Documentation**
# The views.py file in this Django application contains classes that define various views using Django REST Framework. 
# HomeRedirectView:
# This view, HomeRedirectView, is a subclass of APIView.
# It redirects the user to the extend-list URL when they access the root URL.

# ExtendListView:
# This view, ExtendListView, is a subclass of APIView.
# The get method retrieves a list of objects from the Extend model and serializes them using the ExtendSerializer.
# The post method handles the creation of new Extend objects based on the provided data.

# OverdriveView:
# This view, OverdriveView, is a subclass of APIView.
# The get method retrieves either a specific Overdrive object 
# The post method creates a new Overdrive object.
# The put method updates an existing Overdrive object.
# The delete method deletes an existing Overdrive object.

# HormoneView:
# This view, HormoneView, is a subclass of APIView.
# The get method retrieves a list of all Hormone objects.
# The post method creates a new Hormone object.
# The put method updates an existing Hormone object.
# The delete method deletes an existing Hormone object.

# These views utilize serializers (ExtendSerializer, OverdriveSerializer, and HormoneSerializer) 
# is to convert the models into native Python data types that can be easily rendered into JSON responses. 
# The views handle various HTTP methods (GET, POST, PUT, DELETE) 
# to perform CRUD operations on the corresponding models (Extend, Overdrive, Hormone) in the Django application.




# Import modules/packages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect
from .models import Extend
from .serializers import (ChoiceSerializer, ExtendSerializer)
from .Components.carousel import Carousel
from rest_framework.decorators import api_view
from accounts.views import UserRegistrationChoiceView


import requests

# HOMEPAGE

class HomeRedirectView(APIView):
    def get(self, request):
        try:

            # Fetch news using Carousel class
            carousel = Carousel(user_location='WashingtonPost')
            news_items = carousel.fetch_news()

            # Fetch registration choices
            registration_choices_response = requests.get('http://127.0.0.1:8000/api/accounts/registration-choices/')
            registration_choices_response.raise_for_status()
            registration_choices_data = registration_choices_response.json()

            # Fetch login choices
            login_choices_url = 'http://127.0.0.1:8000/api/accounts/login-choices/'
            login_choices_response = requests.get(login_choices_url)
            login_choices_data = login_choices_response.json()

            # Fetch extends data
            extends_data = Extend.objects.all()
            extends_serializer = ExtendSerializer(extends_data, many=True)

            

            response_data = {
                'news': news_items,
                'extends': extends_serializer.data,
                'registration': registration_choices_data,
                'login': login_choices_data,
            }

            return Response(response_data, status=status.HTTP_200_OK)

        except requests.exceptions.RequestException as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
   






