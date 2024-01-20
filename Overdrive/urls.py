# Overdrive/urls.py



# Import modules/packages
from django.urls import path
from .views import (
        OverdriveView, 
        OverdriveUserView, 
        OverdriveProducerView, 
        update_energy_forecast_news,
    )

# Define the URL patterns for the app
urlpatterns = [


    # URLs for Overdrive (Overdrive)
    path('overdrive/', OverdriveView.as_view(), name='overdrive'),
    # path('overdrive/', OverdriveView.as_view(), name='overdrive-list'),
    path('overdrive/<int:pk>/', OverdriveView.as_view(), name='overdrive-detail'),

    # URLs for OverdriveUserView (Overdrive User)
    path('overdrive/user', OverdriveUserView.as_view(), name='overdrive-user-list'),
    path('overdrive/user/<int:pk>/', OverdriveUserView.as_view(), name='overdrive-detail'),

    # URLs for OverdriveProducerView (Overdrive Producer)
    path('overdrive/producer/', OverdriveProducerView.as_view(), name='overdrive-producer-list'),
    path('overdrive/producer/<int:pk>/', OverdriveProducerView.as_view(), name='overdrive-producer-detail'),

    # URL for updating energy forecast news
    path('overdrive/producer/<int:producer_id>/update-energy-forecast-news/', update_energy_forecast_news, name='update-energy-forecast-news'),
]







