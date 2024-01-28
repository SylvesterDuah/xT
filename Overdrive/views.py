# Overdrive/viewps.py





# Import modules/packages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.shortcuts import render, redirect, get_object_or_404


from .models import (
    Overdrive, 
    OverdriveUser, 
    OverdriveProducer, 
    EnergyTreeGrowth
)


from .serializers import (
    OverdriveSerializer,
    OverdriveUserSerializer, 
    OverdriveProducerSerializer,
)



from rest_framework.decorators import api_view
import matplotlib.pyplot as plt
from django.db.models import JSONField
from django.utils import timezone
from django.http import JsonResponse, Http404

   


        




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
        



class OverdriveUserView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = OverdriveUser.objects.all()
    serializer_class = OverdriveUserSerializer

    def generate_storage_capacity_graph(self, overdrive_user):
        if overdrive_user.storage_capacity_data:
            time_values = [entry['time'] for entry in overdrive_user.storage_capacity_data]
            capacity_values = [entry['storage_capacity'] for entry in overdrive_user.storage_capacity_data]

            plt.plot(time_values, capacity_values)
            plt.xlabel('Time')
            plt.ylabel('Storage Capacity')
            plt.title('Storage Capacity Graph')
            plt.grid(True)
            graph_path = f'storage_capacity_graph_{overdrive_user.id}.png'
            plt.savefig(graph_path)
            plt.close()
            return graph_path
        return None

    def generate_energy_consumption_graph(self, overdrive_user):
        if overdrive_user.current_energy_consumption is not None:
            time_value = timezone.now() 
            consumption_value = overdrive_user.current_energy_consumption

            plt.plot(time_value, consumption_value, marker='o')
            plt.xlabel('Time')
            plt.ylabel('Energy Consumption')
            plt.title('Energy Consumption Graph')
            plt.grid(True)
            graph_path = f'energy_consumption_graph_{overdrive_user.id}.png'
            plt.savefig(graph_path)
            plt.close()
            return graph_path
        return None

    def include_energy_tracking_status(self, overdrive_user, serializer_data):
        serializer_data['energy_tracking_status'] = 'Enabled' if overdrive_user.energy_tracking_feature else 'Disabled'

    def include_smart_meters(self, overdrive_user, serializer_data):
        serializer_data['smart_meters_feature'] = overdrive_user.smart_meters_feature

    def generate_energy_tree_growth_chart(self, overdrive_user):
        # Get the EnergyTreeGrowth objects related to this user
        energy_growths = EnergyTreeGrowth.objects.filter(user__id=overdrive_user)

        # Create a line chart showing seed and plant growth over time
        timestamps = [entry.timestamp for entry in energy_growths]
        seed_growth_values = [entry.seed_growth for entry in energy_growths]
        plant_growth_values = [entry.plant_growth for entry in energy_growths]

        plt.plot(timestamps, seed_growth_values, label='Seed Growth')
        plt.plot(timestamps, plant_growth_values, label='Plant Growth')

        plt.xlabel('Timestamp')
        plt.ylabel('Growth')
        plt.title('Energy Tree Growth Chart')
        plt.legend()
        plt.grid(True)

        # Save the chart to a file
        chart_file = f'energy_tree_growth_chart_user_{overdrive_user}.png'
        plt.savefig(chart_file)

        # Close the plot to free up resources
        plt.close()

        return chart_file
    
    def update_energy_forecast_news(self, overdrive_user, latest_energy_forecast_news):
        overdrive_user.energy_forecast_news = latest_energy_forecast_news
        overdrive_user.save()



    @api_view(['POST'])
    def update_energy_forecast_news(self, request, pk):
        try:
            overdrive_user = self.get_object(pk)
            latest_energy_forecast_news = request.data.get('energy_forecast_news', '')
            self.update_energy_forecast_news(overdrive_user, latest_energy_forecast_news)
            response_data = {'message': 'Energy forecast news updated successfully.'}
            return Response(response_data, status=status.HTTP_200_OK)

        except OverdriveUser.DoesNotExist:
            raise Http404("OverdriveUser not found.")



    def get(self, request, pk=None):
        try:
            if pk is not None:
                # Retrieve details of a specific user
                overdrive_user = get_object_or_404(OverdriveUser, id=pk)
                serializer = OverdriveUserSerializer(overdrive_user)
                serializer_data = serializer.data

                # Include additional data
                self.include_energy_tracking_status(overdrive_user, serializer_data)
                
                # Generate and include graphs in the response
                serializer_data['storage_capacity_graph'] = self.generate_storage_capacity_graph(overdrive_user)
                serializer_data['energy_consumption_graph'] = self.generate_energy_consumption_graph(overdrive_user)
                serializer_data['energy_tree_growth_chart'] = self.generate_energy_tree_growth_chart(overdrive_user)

                return Response(serializer_data, status=status.HTTP_200_OK)
            else:
                # List all users
                queryset = self.filter_queryset(self.get_queryset())
                serializer = self.get_serializer(queryset, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)

        except OverdriveUser.DoesNotExist:
            return Response({'error': 'OverdriveUser not found'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'error': f'Unexpected error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





    


# Overdriver Producer
class OverdriveProducerView(APIView):

    def generate_energy_tree_growth_chart(self):
        # Get the EnergyTreeGrowth objects related to this producer
        energy_growths = EnergyTreeGrowth.objects.filter(producer=self)

        # Create a line chart showing seed and plant growth over time
        timestamps = [entry.timestamp for entry in energy_growths]
        seed_growth_values = [entry.seed_growth for entry in energy_growths]
        plant_growth_values = [entry.plant_growth for entry in energy_growths]

        plt.plot(timestamps, seed_growth_values, label='Seed Growth')
        plt.plot(timestamps, plant_growth_values, label='Plant Growth')

        plt.xlabel('Timestamp')
        plt.ylabel('Growth')
        plt.title('Energy Tree Growth Chart')
        plt.legend()
        plt.grid(True)

        # Save the chart to a file
        chart_file = f'energy_tree_growth_chart_producer_{self.id}.png'
        plt.savefig(chart_file)

        # Close the plot to free up resources
        plt.close()

        return chart_file
    

    def update_energy_forecast_news(self, overdrive_producer, latest_energy_forecast_news):
        overdrive_producer.energy_forecast_news = latest_energy_forecast_news
        overdrive_producer.save()



    @api_view(['POST'])
    def update_energy_forecast_news(self, request, producer_id):
        try:
            overdrive_producer = self.get_object(producer_id)
            latest_energy_forecast_news = request.data.get('energy_forecast_news', '')
            self.update_energy_forecast_news(overdrive_producer, latest_energy_forecast_news)
            response_data = {'message': 'Energy forecast news updated successfully.'}
            return Response(response_data, status=status.HTTP_200_OK)

        except OverdriveProducer.DoesNotExist:
            raise Http404("OverdriveProducer not found.")




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
        # Get the OverdriveUser instance
        overdrive_user = OverdriveUser.objects.get(pk=user_id)

        # Assuming you have received the latest news as a parameter or from some external source
        latest_energy_forecast_news = request.data.get('energy_forecast_news', '')

        # Update the energy forecast news for the OverdriveUser
        overdrive_user.energy_forecast_news = latest_energy_forecast_news
        overdrive_user.save()

        # Respond with a success message or any additional data
        response_data = {'message': 'Energy forecast news updated successfully.'}

        return Response(response_data, status=status.HTTP_200_OK)

    except OverdriveUser.DoesNotExist:
        raise Http404("OverdriveUser not found.")
