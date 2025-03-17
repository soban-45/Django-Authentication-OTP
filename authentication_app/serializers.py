from rest_framework import serializers
from .models import User, OTP
from .utils import send_otp_email

class RequestOTPSerializer(serializers.Serializer):
    username = serializers.CharField()
    print(username,'usermane')
    email = serializers.EmailField()

    def validate(self, data):
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError("Email already registered.")
        send_otp_email(data['email'])
        return data

class VerifyOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp_code = serializers.CharField(max_length=6)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        try:
            otp = OTP.objects.filter(email=data['email'], otp_code=data['otp_code']).latest('created_at')
        except OTP.DoesNotExist:
            raise serializers.ValidationError("Invalid OTP.")
        
        if not otp.is_valid():
            raise serializers.ValidationError("OTP expired.")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['email'],  # Use email as username
            email=validated_data['email'],
            password=validated_data['password']
        )
        OTP.objects.filter(email=validated_data['email']).delete()  # Clean OTPs
        return user
