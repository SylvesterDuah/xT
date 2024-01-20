# Hormone/views.py


# Import modules/packages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect
from .models import Hormone, HormoneProducer, HormoneUser
from .serializers import  (HormoneSerializer, HormoneProducerSerializer, HormoneUserSerializer)
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
    # Handle GET requests to retrieve all HormoneUser objects
    def get(self, request):
        hormone_users = HormoneUser.objects.all()

        # Fetch deals_of_week using the Carousel class
        carousel = Carousel()
        deals_of_week = carousel.deals_of_the_week()

        # Update each HormoneUser instance with the deals_of_week information
        for user in hormone_users:
            user.deals_of_the_week = deals_of_week
            user.save()

        # Serialize the updated hormone_users instances
        serializer = HormoneUserSerializer(hormone_users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Handle POST requests to create a new HormoneUser object
    def post(self, request):
        serializer = HormoneUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle PUT requests to update an existing HormoneUser object by PK
    def put(self, request, pk):
        hormone_user = HormoneUser.objects.get(pk=pk)
        serializer = HormoneUserSerializer(hormone_user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle DELETE requests to delete an existing HormoneUser object by PK
    def delete(self, request, pk):
        hormone_user = HormoneUser.objects.get(pk=pk)
        hormone_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


















class HormoneProducerView(APIView):
    # Handle GET requests to retrieve all Hormone objects
    def get(self, request):
        hormones = HormoneProducer.objects.all()
        serializer = HormoneProducerSerializer(hormones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Handle POST requests to create a new Hormone object
    def post(self, request):
        serializer = HormoneProducerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle PUT requests to update an existing Hormone object by PK
    def put(self, request, pk):
        hormone = HormoneProducer.objects.get(pk=pk)
        serializer = HormoneProducerSerializer(hormone, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle DELETE requests to delete an existing Hormone object by PK
    def delete(self, request, pk):
        hormone = HormoneProducer.objects.get(pk=pk)
        hormone.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    






