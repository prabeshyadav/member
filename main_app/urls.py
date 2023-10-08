from django.urls import path
from .views import RegistrationView,LoginView,VerifyOtp

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('otpverification',VerifyOtp.as_view(),name="otpverification")
]