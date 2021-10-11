from django.shortcuts import render
from rest_framework import serializers
from .serializers import ActivateSerilaizer
from .serializers import UserRegister
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import status
from .models import Wallet

from rest_framework.generics import CreateAPIView,ListAPIView



# Create your views here.

class register(APIView):
    
    def post(self,request,format=None):
        serializer=UserRegister(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['response']='registered'
            data['username']=account.username
            data['email']=account.email
            token,create=Token.objects.get_or_create(user=account)
            data['token']=token.key
        else:
            data=serializer.errors
        return Response(data)
    

# class ActivateWallet(APIView):
#     def post(self,request,format=None):
#         serializer = ActivateSerilaizer(data=request.data)
#         print(request.data.status)
#         if serializers.is_valid():
#             serializer.save()
#             res = {'wallet':'enabled'}
#             return Response(res,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializers.erros)

class ActivateWallet(CreateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = ActivateSerilaizer
               
class ShowWallet(ListAPIView):
    queryset = Wallet.objects.all()
    serializer_class = ActivateSerilaizer
               
class deposit(APIView):
    
    def post(self,request,format=None,id=None):
        serializer=UserRegister(data=request.data)
        id =request.data.get(id)
        cust_id = Wallet.objects.get(id=id)
        if serializers.is_valid():
            serializers.save()     
            return Response(serializers.data)
        return Response(serializers.errors)

            

        