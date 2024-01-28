# Hormone/views.py


# Import modules/packages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect
from .models import Hormone, HormoneProducer, HormoneUser, SellerRating
from .serializers import  (HormoneSerializer, HormoneProducerSerializer, HormoneUserSerializer, SellerRatingSerializer)
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from accounts.views import UserRegistrationChoiceView
from home.Components.carousel import Carousel


import requests

class HormoneView(APIView):
    # Handle GET requests to retrieve all Hormone objects
    def get(self, request):
        hormones = Hormone.objects.all()
        serializer = HormoneSerializer(hormones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Handle POST requests to create a new Hormone object
    def post(self, request):
        serializer = HormoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







# Hormone User
class HormoneUserView(APIView):
    def get(self, request, format=None):
        hormone_users = HormoneUser.objects.all()

        # Fetch deals_of_week using the Carousel class
        carousel = Carousel()
        deals_of_week = carousel.deals_of_the_week()

        # Update each HormoneUser instance with the deals_of_week information
        for user in hormone_users:
            user.deals_of_the_week = deals_of_week
            user.renewable_energy_types = user.get_renewable_energy_types()
            user.top_ingins = user.get_top_ingins()
            user.save()

        # Create a list to store producer information for the landing page
        producers_info = []

        # Fetch information from HormoneProducer
        for hormone_user in hormone_users:
            producer = HormoneProducer.objects.filter(user=hormone_user.user).first()

            if producer:
                producer_info = {
                    'producer_name': producer.user.username,
                    'renewable_energy_types': hormone_user.renewable_energy_types,
                    'top_ingins': hormone_user.top_ingins,
                    'rating': self.calculate_average_rating(producer),
                }
                producers_info.append(producer_info)

        return Response(producers_info, status=status.HTTP_200_OK)

    def calculate_average_rating(self, producer):
        try:
            ratings = SellerRating.objects.filter(seller=producer)
            if ratings.exists():
                average_rating = ratings.aggregate(Avg('rating'))['rating__avg']
                return round(average_rating, 2) if average_rating else None
        except SellerRating.DoesNotExist:
            pass

        return None





















class HormoneProducerView(APIView):
    def get(self, request, format=None):
        hormone_producers = HormoneProducer.objects.all()
        serializer = HormoneProducerSerializer(hormone_producers, many=True)

        # Fetch deals_of_week/trends/unforeseen_features using the Carousel class
        carousel = Carousel()
        deals_of_week = carousel.deals_of_the_week()
        trends = carousel.fetch_trends()
        unforeseen_features = carousel.fetch_unforeseen_features()

        # Update each HormoneProducer instance with the deals_of_week, trends, and unforeseen_features
        for producer in hormone_producers:
            producer.deals_of_the_week = deals_of_week
            producer.trends = trends
            producer.unforeseen_features = unforeseen_features
            producer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = HormoneProducerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['POST'])
def submit_rating(request, seller_id):
    try:
        seller_instance = HormoneProducer.objects.get(pk=seller_id)
    except HormoneProducer.DoesNotExist:
        return Response({"error": "Seller not found"}, status=status.HTTP_404_NOT_FOUND)

    rating_value = request.data.get('rating')
    if rating_value is None:
        return Response({"error": "Rating value is required"}, status=status.HTTP_400_BAD_REQUEST)

    # Validate the rating value if needed

    seller_rating = SellerRating(seller=seller_instance, rating=rating_value)
    seller_rating.save()

    serializer = SellerRatingSerializer(seller_rating)
    return Response(serializer.data, status=status.HTTP_201_CREATED)



