from rest_framework import serializers
import imp
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *
User = get_user_model()
# Create your serializers here.
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","name","phone","gender","gender_intersted_in","looking_for","interest_in","sexual_orientation_in","user_dob"]
        extra_kwargs = {
            "id": {"read_only": True},
            "name": {"required": True},
            "phone": {"required": True},
            "gender": {"required": True},
            "gender_intersted_in": {"required": True},
            "looking_for": {"required": True},
            "interest_in": {"required": True},
            "sexual_orientation_in": {"required": True},
            "user_dob": {"required": True},
            "image": {"required": True},
        }
        
    def create(self, validated_data):
            user = User.objects.create(**validated_data)
            return user
        
class User_get_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields  = '__all__'