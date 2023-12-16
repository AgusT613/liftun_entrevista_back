from rest_framework import serializers
from .models import EnvironmentAction


class EnvironmentActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnvironmentAction
        fields = "__all__"
