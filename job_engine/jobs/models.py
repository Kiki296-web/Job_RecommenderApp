from django.db import models
from users.models import User



class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    required_skills = models.TextField()
    category = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class JobRecommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recommendations")
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="recommendations")
    match_reason = models.TextField()
    recommended_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recommendation for {self.user.username} - {self.job.title}"

