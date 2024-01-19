# important.serializers.py

from .models import UserProfile
from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"


class profile_info(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ["username", "code", "first_name", "last_name"]

    def get_first_name(self, obj):
        return obj.get_first_name()

    def get_last_name(self, obj):
        return obj.get_last_name()

    def get_username(self, obj):
        return obj.get_username()
