from django.urls import path
from .views import *

urlpatterns = [
    path('send-otp/', RequestOTPView.as_view(), name='send-otp'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify-otp'),
        path('register/', RegisterUserView.as_view(), name='register'),

]   
