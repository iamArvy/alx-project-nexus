from rest_framework import serializers
from api.models import Job


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"
        read_only_fields = ("id",)
