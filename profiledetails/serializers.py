from rest_framework import serializers
import imp
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *
User = get_user_model()
# Create your serializers here.
class Upload_image_seriliazer(serializers.ModelSerializer):
    class Meta:
        model = Upload_image
        fields = "__all__"
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
        }
        
    def create(self, validated_data):
            user = User.objects.create(**validated_data)
            return user
        
class User_get_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields  = '__all__'

class Favourite_serializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = "__all__"

class Chatting_serializer(serializers.ModelSerializer):
    class Meta:
        model = Chatting
        fields = "__all__"
        
class Notification_serializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"


from library.sociallib import facebook
from library.register.register import register_social_user
     
class FacebookSocialAuthSerializer(serializers.Serializer):
    """Handles serialization of facebook related data"""
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = facebook.Facebook.validate(auth_token)

        try:
            user_id = user_data['id']
            email = user_data['email']
            name = user_data['name']
            provider = 'facebook'
        except:

            raise serializers.ValidationError(
                'The token  is invalid or expired. Please login again.'
            )
        return register_social_user(
            provider=provider, user_id=user_id, email=email, name=name)