from rest_framework import serializers
from rest_framework.settings import api_settings


class BaseModelSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    created_at = serializers.DateTimeField(format=api_settings.DATE_FORMAT, required=False, read_only=True)
    updated_at = serializers.DateTimeField(format=api_settings.DATE_FORMAT, required=False, read_only=True)

    def update(self, instance, validated_data):
        raise serializers.ValidationError("Your must implement your own update method")

    def create(self, validated_data):
        raise serializers.ValidationError("Your must implement your own create method")
