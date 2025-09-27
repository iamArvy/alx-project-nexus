from rest_framework import serializers
from api.models import Job
from django.utils import timezone


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"
        read_only_fields = (
            "created_at",
            "id",
        )

    def validate_end_date(self, value):
        if value <= timezone.now().date():
            raise serializers.ValidationError("End date must be greater than today.")
        return value
