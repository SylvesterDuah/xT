# Extend/urls.py
# import sys
# print(sys.path)

from django.contrib import admin
from django.urls import path, include
from home.views import HomeRedirectView 
from accounts.views import UserRegistrationChoiceView
from Overdrive.views import OverdriveView, OverdriveProducerView, OverdriveUserView
from Hormone.views import HormoneView, HormoneProducerView, HormoneUserView

urlpatterns = [
    path('admin/', admin.site.urls),
    

    # Accounts urls
    path('api/accounts/', include('accounts.urls')),

    # Extend/Homepage url
    path('', HomeRedirectView.as_view(), name='home-redirect'), 

    # Overdrive urls
    path('overdrive/', OverdriveView.as_view(), name='overdrive'),
    path('overdrive/producers/', OverdriveProducerView.as_view(), name='overdrive-producer-list'),
    path('overdrive/users/', OverdriveUserView.as_view(), name='overdrive-user-list'),

    # Hormone urls
    path('hormone/', HormoneView.as_view(), name='hormone'),
    path('hormones/producers/', HormoneProducerView.as_view(), name='hormone-producer-list'),
    path('hormones/users/', HormoneUserView.as_view(), name='hormone-user-list'),
    
]



