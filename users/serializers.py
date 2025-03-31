from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data('first_name', ''),
            last_name=validated_data('last_name', '')
        )
        return user


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'avatar', 'bio')

