from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import RequestOTPSerializer, VerifyOTPSerializer

class RequestOTPView(APIView):
    def post(self, request):
        print(request.data)
        serializer = RequestOTPSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"message": "OTP sent to your email."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyOTPView(APIView):
    def post(self, request):
        serializer = VerifyOTPSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Registration successful."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
