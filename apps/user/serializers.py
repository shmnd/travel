# apps/users/api/serializers.py
from rest_framework import serializers

class SuperAdminLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True, style={'input_type': 'password'})
