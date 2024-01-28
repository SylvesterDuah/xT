# Hormone/urls.py

# Import modules/packages
from django.urls import path
from .views import HormoneView, HormoneProducerView, HormoneUserView, submit_rating

# Define the URL patterns for the app
urlpatterns = [
    # URLs for HormonerView (Hormone)
    path('hormone/', HormoneView.as_view(), name='hormone'),

    # URLs for HormoneProducerView (Hormone Producer)
   path('producers/', HormoneProducerView.as_view(), name='hormone-producer-list'),


    # Add a detail view for individual producers if needed
    path('producer/<int:pk>/', HormoneUserView.as_view(), name='hormone-producer-detail'),

    # URLs for HormoneUserView (Hormone User)
    path('user/', HormoneUserView.as_view(), name='hormone-user-list'),
    path('hormones/user/<int:pk>/', HormoneUserView.as_view(), name='hormone-user-detail'),



    path('submit_rating/<int:seller_id>/', submit_rating, name='submit_rating'),
]
