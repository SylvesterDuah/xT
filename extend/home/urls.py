from django.urls import path
from .views import ExtendListView, OverdriveView, HormoneView, HomeRedirectView

urlpatterns = [
    path('', HomeRedirectView.as_view(), name='home-redirect'),  # Redirect root URL to extend-list
    path('extend/', ExtendListView.as_view(), name='extend-list'),

    

    # Overdrive - PowerWall
    path('overdrive/', OverdriveView.as_view(), name='overdrive-list'),
    path('overdrive/<int:pk>/', OverdriveView.as_view(), name='overdrive-detail'),
    
    
    # Hormone - Ecommerce
    path('hormones/', HormoneView.as_view(), name='hormones-list'),
    path('hormones/<int:pk>/', HormoneView.as_view(), name='hormones-detail'),
    path('hormones/<int:pk>/producer-dashboard/', HormoneView.as_view(), name='producer-dashboard'),
]


