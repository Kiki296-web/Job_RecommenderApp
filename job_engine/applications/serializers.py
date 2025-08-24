from rest_framework import serializers
from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    job_title = serializers.ReadOnlyField(source="job.title")

    class Meta:
        model = Application
        fields = ["id", "user", "job", "job_title", "status", "applied_date"]
        read_only_fields = ["user", "applied_date"]
