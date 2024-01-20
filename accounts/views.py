# accounts/views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import SellerRegistrationSerializer
from .models import User  



# Rest_Framework View 
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView


# Redirect for Pop up message of Registration
from django.shortcuts import redirect


















# Registration choice
class UserRegistrationChoiceView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'detail': 'Choose registration type'}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        registration_type = request.data.get('registration_type')

        if registration_type == 'buyer':
            return redirect('buyer-registration')
        elif registration_type == 'seller':
            return redirect('seller-registration')
        else:
            return Response({'detail': 'Invalid registration type'}, status=status.HTTP_400_BAD_REQUEST)







 





class SellerRegistrationCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SellerRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            # Extract relevant user information
            user_data = {
                'username': serializer.validated_data['user']['username'],
                'email': serializer.validated_data['user']['email'],
                'password': serializer.validated_data['user']['password'],
            }

            # Create the user
            user = User.objects.create_user(**user_data)

            # Create the seller
            seller = serializer.save(user=user)

            return Response({'message': 'Seller created successfully.'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



        

# User Login View
class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user:
            # If authentication is successful, log the user in
            login(request, user)
            return Response({'detail': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            # If authentication fails, return an error response
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class YourLoginChoicesView(APIView):
    def get(self, request, *args, **kwargs):
        login_choices = [
            {'value': 'buyer', 'label': 'Login as Buyer'},
            {'value': 'seller', 'label': 'Login as Seller'},
        ]

        return Response({'login_choices': login_choices}, status=status.HTTP_200_OK)   



    
# User Logout View
class UserLogoutView(APIView):
    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({'detail': 'Logout successful'}, status=status.HTTP_200_OK)
