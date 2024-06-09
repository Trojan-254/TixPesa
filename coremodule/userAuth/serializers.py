from rest_framework import serializers
from django.contrib.auth.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    """Serializes user data for registration."""
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        """Meta class for UserRegistrationSerializer."""
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

    def validate(self, data):
        """Validates the password and password2 fields."""
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError("User with this email already exists.")
        return data

    def create(self, validated_data):
        """Creates a new user."""
        user = User(
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            email=validated_data.get('email'),
            username=validated_data.get('email')
        )
        user.set_password(validated_data['password1'])
        user.is_active = False  # User is inactive until email verification
        user.save()
        return user
