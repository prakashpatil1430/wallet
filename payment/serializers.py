import uuid
from django.db import models
from django.db.models import fields
from rest_framework import serializers, status
from django.contrib.auth import get_user_model
from .models import Wallet

User=get_user_model()

class UserRegister(serializers.ModelSerializer):
    
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    # id = serializers.UUIDField(required = False)
    
    
    class Meta:
        model=User
        id = models.UUIDField(primary_key = True,default = uuid.uuid4, editable = False)
        fields=["id","username","password","email","password2"]
        
    def save(self):
        reg=User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError({'password':'password does not match'})
        reg.set_password(password)
        reg.save()
        return reg

class ActivateSerilaizer(serializers.ModelSerializer):

    status = serializers.BooleanField(default=False)

    def validate_status(self,value):
        if value ==False:
            data = Wallet.objects.get('status').update(status=True)
        else:
            raise serializers.ValidationError("waleet activated alreadt")
        
            
            
    class Meta:
        model = Wallet
        fields = "__all__"


    



# class UserDataSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields=["id",'username','email','first_name','last_name']