# Extend/urls.py
# import sys
# print(sys.path)

from django.contrib import admin
from django.urls import path, include
from home.views import HomeRedirectView 
from accounts.views import UserRegistrationChoiceView
from Overdrive.views import OverdriveView
from Hormone.views import HormoneView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Accounts urls
    path('api/accounts/', include('accounts.urls')),

    # Extend/Homepage url
    path('', HomeRedirectView.as_view(), name='home-redirect'), 

    # Overdrive urls
    path('overdrive/', OverdriveView.as_view(), name='overdrive'),

    # Hormone urls
    path('hormone/', HormoneView.as_view(), name='hormone'),
]



