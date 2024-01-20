# Hormone/urls.py


# Import modules/packages
from django.urls import path
from .views import HormoneView, HormoneProducerView, HormoneUserView

# Define the URL patterns for the app
urlpatterns = [
    # URLs for HormonerView (Hormone)
    path('hormone/', HormoneView.as_view(), name='hormone'),

    # URLs for HormoneProducerView (Hormone Producer)
    path('hormones/producer/', HormoneProducerView.as_view(), name='hormone-producer-list'),
    path('hormones/producer/<int:pk>/', HormoneProducerView.as_view(), name='hormone-producer-detail'),

    # URLs for HormoneUserView (Hormone User)
    path('hormones/user/', HormoneUserView.as_view(), name='hormone-user-list'),
    path('hormones/user/<int:pk>/', HormoneUserView.as_view(), name='hormone-user-detail'),
]
