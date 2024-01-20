# accounts/urls.py
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    UserLoginView, UserLogoutView,
    UserRegistrationChoiceView, YourLoginChoicesView
)
from Hormone.views import HormoneProducerView



urlpatterns = [
    # Registration Views
    path('register/', UserRegistrationChoiceView.as_view(), name='user_registration_choice'),
    path('registration-choices/', UserRegistrationChoiceView.as_view(), name='registration-choices'),
    # path('register/buyer/', BuyerRegistrationView.as_view(), name='buyer-registration'),
    # path('register/seller/', SellerRegistrationView.as_view(), name='seller-registration'),



    # path('api/accounts/register/seller/', UserRegistrationView.as_view(), name='user-registration'),

    # User profile View
    # path('profile/', UserProfileView.as_view(), name='user_profile'),


    # Authentication Views
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
    path('login-choices/', YourLoginChoicesView.as_view(), name='login-choices'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),



    # URL for Hormone Producer View at the Home app
    path('hormones/producer/', HormoneProducerView.as_view(), name='hormone-producer-list'),
    path('hormones/producer/<int:pk>/', HormoneProducerView.as_view(), name='hormone-producer-detail'),

]
