from rest_framework.views import APIView
from .serializers import ProductSerialzier
from .models import Product
from rest_framework.response import Response
from rest_framework import serializers
from decouple import config
from django.contrib.auth.models import User


class AuthenticationBody(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class Authenticator(APIView):
    def post(self,request):
        body = AuthenticationBody(data=request.data)
        if body.is_valid():
            new_user,created = User.objects.get_or_create(username=body.validated_data["username"])
            print(new_user)
            if created:
                new_user.set_password(body.validated_data["password"])
                new_user.save()
            if new_user.check_password(body.validated_data["password"]):
                return Response({'message':'success'})
            else:
                return Response({'message':"Incorrect password"},status=401)
        return Response({'message':body.errors})


class ProductView(APIView):
    query_set = Product.objects.all()
    def get(self,request):
        return Response(ProductSerialzier(self.query_set,many=True).data)

    def post(self,request):
        body = ProductSerialzier(data=request.data)

        if body.is_valid():
            body.save()
            return Response({'message','Ok!'})
        return Response({'message':body.errors})