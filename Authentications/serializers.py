from django.db.models.base import Model
from rest_framework import fields, serializers
from .models import LoginUser

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginUser
        fields = ('mobileNo', 'password')
            
