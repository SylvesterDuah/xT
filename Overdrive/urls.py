from django.urls import path
from .views import (
    OverdriveView,
    OverdriveUserView,
    OverdriveProducerView,
    update_energy_forecast_news,
)

urlpatterns = [
    path('overdrive/', OverdriveView.as_view(), name='overdrive'),

    # Assuming you want OverdriveUserView to handle both list and detail views
    path('overdrive/users/', OverdriveUserView.as_view(), name='overdrive-user-list'),
    path('overdrive/users/<int:pk>/', OverdriveUserView.as_view(), name='overdrive-user-detail'),

    # Update Energy Forecast News
    path('overdrive/producers/<int:producer_id>/update-energy-forecast-news/', update_energy_forecast_news, name='update-energy-forecast-news'),
    # path('overdrive/producers/<int:producer_id>/update-energy-forecast-news/', update_energy_forecast_news, name='update-energy-forecast-news'),


    # Producers
    path('overdrive/producers/', OverdriveProducerView.as_view(), name='overdrive-producers'),
    
]
