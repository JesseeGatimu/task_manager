from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer,LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
def get_token_for_user(user):
    refresh=RefreshToken.for_user(user)
    return {
        'refresh':str(refresh),
        'access':str(refresh.access_token)
    }

class RegisterAPI(APIView):
    def post(self,request):
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            tokens=get_token_for_user(user)
            return Response({
                'message':'User registered successfully',
                'tokens':tokens
            },status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class LoginAPI(APIView):
    def post(self,request):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            user=authenticate(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            if user is not None:
                tokens=get_token_for_user(user)
                return Response({
                    'message':'Login Successfully',
                    'tokens':tokens
                },status=status.HTTP_200_OK)
            return Response({
                'error':'User not found'
            },status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class LogoutAPI(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        try:
            refresh_token=request.data['refresh']
            tokens=RefreshToken(refresh_token)
            tokens.blacklist()
            return Response({
                'message':'Logout successful'
            },status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response({
                'error':'Invalid Tokens'
            },status=status.HTTP_400_BAD_REQUEST)