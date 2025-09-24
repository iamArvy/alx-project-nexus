from rest_framework import serializers
from api.models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    applicant = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Application
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at", "id", "status", "applicant")

    def update(self, instance, validated_data):
        """
        Prevent updates except status (which is handled in a special view).
        """
        raise serializers.ValidationError(
            "Applications cannot be updated after creation."
        )

    def validate(self, data):
        job = data.get("job")
        applicant = data.get("applicant")

        if Application.objects.filter(job=job, applicant=applicant).exists():
            raise serializers.ValidationError("You have already applied for this job.")
        return data
