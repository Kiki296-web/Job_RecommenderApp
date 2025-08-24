from rest_framework import serializers
from .models import Job, JobRecommendation

class JobSerializer(serializers.ModelSerializer):
    posted_by = serializers.ReadOnlyField(source="posted_by.username")  # This shows username instead of ID

    class Meta:
        model = Job
        fields = ["id", "title", "description", "required_skills", "category", "location", "posted_date", "posted_by"]


class JobRecommendationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    job = JobSerializer(read_only=True)

    class Meta:
        model = JobRecommendation
        fields = ["id", "user", "job", "match_reason", "recommended_at"]
