from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['organization_name', 'first_name', 'last_name', 'email', 'phone_number', 'subdomain', 'password','is_verified']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = CustomUser(
            organization_name=validated_data['organization_name'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            subdomain=validated_data['subdomain'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    
    
class CustomUserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = authenticate(email=email, password=password)

        if not user:
            raise serializers.ValidationError('Invalid login credentials')

        if not user.is_active:
            raise serializers.ValidationError('User account is not active')

        data['user'] = user
        return data


class AccountVerificationOtp(serializers.Serializer):
    email=serializers.CharField()
    otp=serializers.CharField()
    
