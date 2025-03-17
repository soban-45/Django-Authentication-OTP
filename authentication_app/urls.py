from django.urls import path
from .views import RequestOTPView, VerifyOTPView

urlpatterns = [
    path('send-otp/', RequestOTPView.as_view(), name='send-otp'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify-otp'),
]
