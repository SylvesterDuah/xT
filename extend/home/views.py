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
from .models import Extend, Overdrive, Hormone
from .serializers import ExtendSerializer, OverdriveSerializer, HormoneSerializer









# HOMEPAGE
class HomeRedirectView(APIView):
    # Handle GET requests to redirect to the 'extend-list' URL
    def get(self, request):
        return redirect('extend-list')

# Forms of extend page
class ExtendListView(APIView):
    # Handle GET requests to retrieve all Extend objects
    def get(self, request):
        extend = Extend.objects.all()
        serializer = ExtendSerializer(extend, many=True)
        return Response(serializer.data)

    # Handle POST requests to create a new Extend object
    def post(self, request):
        # Print the request data to the console
        print("Request Data:", request.data)

        serializer = ExtendSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# OVERDRIVE
class OverdriveView(APIView):
    # Helper function to get an Overdrive object by its primary key
    def get_object(self, pk):
        try:
            return Overdrive.objects.get(pk=pk)
        except Overdrive.DoesNotExist:
            return None

    # Handle GET requests to retrieve all Overdrive objects or a specific one by PK
    def get(self, request, pk=None):
        if pk is not None:
            overdrive = self.get_object(pk)
            if overdrive:
                serializer = OverdriveSerializer(overdrive)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'message': 'Overdrive not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            overdrives = Overdrive.objects.all()
            serializer = OverdriveSerializer(overdrives, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Handle POST requests to create a new Overdrive object
    def post(self, request):
        serializer = OverdriveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Handle PUT requests to update an existing Overdrive object by PK
    def put(self, request, pk):
        overdrive = self.get_object(pk)
        if overdrive:
            serializer = OverdriveSerializer(overdrive, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Overdrive not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # Handle DELETE requests to delete an existing Overdrive object by PK
    def delete(self, request, pk):
        overdrive = self.get_object(pk)
        if overdrive:
            overdrive.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'message': 'Overdrive not found'}, status=status.HTTP_404_NOT_FOUND)

# HORMONE
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

    # Handle PUT requests to update an existing Hormone object by PK
    def put(self, request, pk):
        hormone = Hormone.objects.get(pk=pk)
        serializer = HormoneSerializer(hormone, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle DELETE requests to delete an existing Hormone object by PK
    def delete(self, request, pk):
        hormone = Hormone.objects.get(pk=pk)
        hormone.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
