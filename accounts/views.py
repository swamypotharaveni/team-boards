from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from.serializers import RegisterSerializers,UserSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from.models import EmailVerifiecation
from django.core.mail import send_mail
from team_bords.settings import EMAIL_HOST_USER
class UserRegitser(APIView):
    def post(self, request, *args, **kwargs):
        email=request.data.get("email",None)
        username=request.data.get("username",None)
        password=request.data.get("password",None)
        serialiser=RegisterSerializers(data=request.data)
        if serialiser.is_valid():
            user=serialiser.save()
            return Response( {"status": "success", "message": "User registered successfully"},status=status.HTTP_201_CREATED)
        return Response(serialiser.errors,status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):
    def post(self, request, *args, **kwargs):
        email=request.data.get("email",None)
        password=request.data.get("password",None)
        user=authenticate(email=email,password=password)
        if not user:
            return Response({"error","Invalid email or password"},status=status.HTTP_400_BAD_REQUEST)
        if not user.is_verified:
            return Response({"error": "Email not verified"}, status=400)

        token,creted=Token.objects.get_or_create(user=user)
        return Response({
            "token": token.key,
            "user": {
                "id": str(user.id),
                "email": user.email,
                "username": user.username
            }
        }, status=200)
    

class UserDetail(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        serializer=UserSerializers(request.user)
        return Response(serializer.data)
class VerifyEmail(APIView):
    def get(self,request,token):
        try:
            record =EmailVerifiecation.objects.get(token=token)
            user=record.user
            user.is_verified=True
            user.save()
            record.delete()
            # return Response({"message": "Email verified successfully!"})
            return render(request, "email_verified.html")
        except EmailVerifiecation.DoesNotExist:
            return render(request, "email_invalid.html")
            #   return Response({"error": "Invalid or expired token"}, status=400)