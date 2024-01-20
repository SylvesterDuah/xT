# Overdrive/viewps.py





# Import modules/packages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect
from .models import Overdrive, OverdriveUser, OverdriveProducer
from .serializers import (
    OverdriveSerializer,
    OverdriveUserSerializer, OverdriveProducerSerializer,
)

from rest_framework.decorators import api_view

   


        




# OVERDRIVE
class OverdriveView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            overdrive = self.get_object(pk)
            if overdrive:
                serializer = OverdriveSerializer(overdrive)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'message': 'Overdrive not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            # Get the first Overdrive instance (you might want to adjust this logic based on your requirements)
            overdrive = Overdrive.objects.first()
            if overdrive:
                # Serialize the required fields
                serialized_data = {
                    'description': overdrive.description,
                    'overdrive_image': overdrive.overdrive_image.url if overdrive.overdrive_image else None,
                    'models_and_specifications': overdrive.models_and_specifications,
                    'key_benefits': overdrive.key_benefits,
                    'getting_started_guide': overdrive.getting_started_guide,
                    'pricing_information': overdrive.pricing_information,
                    'customer_testimonials': overdrive.customer_testimonials,
                    'sustainability_commitment': overdrive.sustainability_commitment,
                }
                return Response(serialized_data, status=status.HTTP_200_OK)
            return Response({'message': 'No Overdrive instance found'}, status=status.HTTP_404_NOT_FOUND)





class OverdriveUserView(APIView):
    def get(self, request, pk=None):
        print(f"Handling GET request for Overdrive objects. PK: {pk}")
        if pk is not None:
            overdrive = self.get_object(pk)
            if overdrive:
                serializer = OverdriveUserSerializer(overdrive)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'message': 'Overdrive not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            overdrives = OverdriveUser.objects.all()
            serializer = OverdriveUserSerializer(overdrives, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    
    # Handle POST requests to create a new Overdrive object
    def post(self, request):
        serializer = OverdriveUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Handle PUT requests to update an existing Overdrive object by PK
    def put(self, request, pk):
        overdrive = self.get_object(pk)
        if overdrive:
            serializer = OverdriveUserSerializer(overdrive, data=request.data)
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



# Overdriver Producer
class OverdriveProducerView(APIView):
    # Helper function to get an OverdriveProducer object by its primary key
    def get_object(self, pk):
        try:
            return OverdriveProducer.objects.get(pk=pk)
        except OverdriveProducer.DoesNotExist:
            return None

    # Handle GET requests to retrieve all OverdriveProducer objects or a specific one by PK
    def get(self, request, pk=None):
        if pk is not None:
            overdrive_producer = self.get_object(pk)
            if overdrive_producer:
                serializer = OverdriveProducerSerializer(overdrive_producer)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'message': 'OverdriveProducer not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            overdrive_producers = OverdriveProducer.objects.all()
            serializer = OverdriveProducerSerializer(overdrive_producers, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    # Handle POST requests to create a new OverdriveProducer object
    def post(self, request):
        serializer = OverdriveProducerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle PUT requests to update an existing OverdriveProducer object by PK
    def put(self, request, pk):
        overdrive_producer = self.get_object(pk)
        if overdrive_producer:
            serializer = OverdriveProducerSerializer(overdrive_producer, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'OverdriveProducer not found'}, status=status.HTTP_404_NOT_FOUND)

    # Handle DELETE requests to delete an existing OverdriveProducer object by PK
    def delete(self, request, pk):
        overdrive_producer = self.get_object(pk)
        if overdrive_producer:
            overdrive_producer.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'message': 'OverdriveProducer not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])  
def update_energy_forecast_news(request, producer_id):
    try:
        # Get the OverdriveProducer instance
        overdrive_producer = OverdriveProducer.objects.get(pk=producer_id)

        # Assuming you have received the latest news as a parameter or from some external source
        latest_energy_forecast_news = "Latest energy forecast news for your OverdriveProducer."

        # Update the energy forecast news for the OverdriveProducer
        overdrive_producer.update_energy_forecast_news(latest_energy_forecast_news)

        # Respond with a success message or any additional data
        response_data = {'message': 'Energy forecast news updated successfully.'}

        return Response(response_data, status=status.HTTP_200_OK)

    except OverdriveProducer.DoesNotExist:
        # Handle the case where the OverdriveProducer is not found
        error_data = {'error': 'OverdriveProducer not found.'}
        return Response(error_data, status=status.HTTP_404_NOT_FOUND)


