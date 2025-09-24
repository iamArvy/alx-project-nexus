from rest_framework import serializers
from api.models import Industry


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = "__all__"
        read_only_fields = ("id",)
