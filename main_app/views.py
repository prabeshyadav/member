from django.shortcuts import render

from rest_framework import status
from .serializers import CustomUserSerializer,CustomUserLoginSerializer,AccountVerificationOtp
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from .models import CustomUser

from rest_framework.views import APIView
from rest_framework.response import Response
from .emails import send_otp_via_email

class RegistrationView(APIView):
    def post(self, request):
        try:
            serializer = CustomUserSerializer(data=request.data)
            
            if serializer.is_valid():
                user = serializer.save()  # Save the user object
                
                # Send OTP email after saving the user
                send_otp_via_email(user.email)  # Use the user's email directly
                
                return Response({
                    "message": "Registration successful",
                    "data": serializer.data,
                }, status=status.HTTP_201_CREATED)  # Use status code 201 for successful creation
            
            # If serializer is not valid, return errors
            return Response({
                "message": "Registration failed",
                "errors": serializer.errors,  # Include serializer validation errors
            }, status=status.HTTP_400_BAD_REQUEST)  # Use status code 400 for bad request
        
        except Exception as e:
            print(e)  # You can log the exception for debugging
            return Response({
                "message": "Internal server error",
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoginView(APIView):
    def post(self, request):
        serializer = CustomUserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            user = authenticate(request, email=email, password=password)

            if user is not None:
                # Log the user in
                django_login(request, user)
                return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Invalid login credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class VerifyOtp(APIView):
    def post(self, request):
        try:
            serializer =AccountVerificationOtp(data=request.data)
            
            if serializer.is_valid():
                email=serializer.data('email')
                otp=serializer.data('otp')
                
                user=CustomUser.objects.filter(email=email)
                if not user.exists():
                    return Response({
                "status":400,
                "message": "something went wrong",
                "data":'invalid otp'  # Include serializer validation errors
                })
                    
                if user[0].otp !=otp:
                    return Response({
                "status":400,
                "message": "something went wrong",
                "data":'invalid otp'  # Include serializer validation errors
                })
                    
                user=user.first()
                user.is_verified=True
                user.save()
                
                return Response({
                "status":400,
                "message": "account is veriffied",
                "data":{}  # Include serializer validation errors
                })
                        
            return Response({
                "message": "Registration failed",
                "errors": serializer.errors,  # Include serializer validation errors
            }, status=status.HTTP_400_BAD_REQUEST)     
                
                
            
            
        except Exception as e:
            print(e)  # You can log the exception for debugging
            return Response({
                "message": "Internal server error",
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)