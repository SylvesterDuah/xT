# Import modules/packages
from django.urls import path
from .views import  HomeRedirectView

# Define the URL patterns for the app
urlpatterns = [
    # Root URL redirects to 'extend-list'
    path('', HomeRedirectView.as_view(), name='xT'),
]
