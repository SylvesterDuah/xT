from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect
from .models import Extend, Overdrive, Hormone
from .serializers import ExtendSerializer, OverdriveSerializer, HormoneSerializer












# HOMEPAGE
class HomeRedirectView(APIView):
    def get(self, request):
        return redirect('extend-list')


# Forms of extend page
class ExtendListView(APIView):
    def get(self, request):
        extend = Extend.objects.all()
        serializer = ExtendSerializer(extend, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ExtendSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)











# OVERDRIVE
class OverdriveView(APIView):
    def get_object(self, pk):
        try:
            return Overdrive.objects.get(pk=pk)
        except Overdrive.DoesNotExist:
            return None

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
    
    def post(self, request):
        serializer = OverdriveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        overdrive = self.get_object(pk)
        if overdrive:
            serializer = OverdriveSerializer(overdrive, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Overdrive not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk):
        overdrive = self.get_object(pk)
        if overdrive:
            overdrive.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'message': 'Overdrive not found'}, status=status.HTTP_404_NOT_FOUND)












# HORMONE
class HormoneView(APIView):
    def get(self, request):
        hormones = Hormone.objects.all()
        serializer = HormoneSerializer(hormones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = HormoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        hormone = Hormone.objects.get(pk=pk)
        serializer = HormoneSerializer(hormone, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        hormone = Hormone.objects.get(pk=pk)
        hormone.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

