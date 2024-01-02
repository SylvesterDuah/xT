# Import modules/packages
from django.urls import path
from .views import ExtendListView, OverdriveView, HormoneView, HomeRedirectView

# Define the URL patterns for the app
urlpatterns = [
    # Root URL redirects to 'extend-list'
    path('', HomeRedirectView.as_view(), name='home-redirect'),

    # URL for ExtendListView, mapped to 'extend-list'
    path('extend/', ExtendListView.as_view(), name='extend-list'),

    # URLs for OverdriveView (PowerWall)
    path('overdrive/', OverdriveView.as_view(), name='overdrive-list'),
    path('overdrive/<int:pk>/', OverdriveView.as_view(), name='overdrive-detail'),
    
    # URLs for HormoneView (Ecommerce)
    path('hormones/', HormoneView.as_view(), name='hormones-list'),
    path('hormones/<int:pk>/', HormoneView.as_view(), name='hormones-detail'),
    path('hormones/<int:pk>/producer-dashboard/', HormoneView.as_view(), name='producer-dashboard'),
]
