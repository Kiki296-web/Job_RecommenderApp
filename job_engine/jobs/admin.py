from django.contrib import admin
from .models import Job, JobRecommendation

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "location", "posted_by", "posted_date")
    search_fields = ("title", "category", "location", "required_skills")
    list_filter = ("category", "location", "posted_date")

@admin.register(JobRecommendation)
class JobRecommendationAdmin(admin.ModelAdmin):
    list_display = ("user", "job", "match_reason", "recommended_at")
    search_fields = ("user__username", "job__title")
    list_filter = ("recommended_at",)
