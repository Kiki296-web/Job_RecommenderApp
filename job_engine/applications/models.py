from django.db import models
from users.models import User
from jobs.models import Job

class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications")
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applications")
    status = models.CharField(max_length=50,
        choices=[
            ("applied", "Applied"),
            ("shortlisted", "Shortlisted"),
            ("rejected", "Rejected"),
            ("hired", "Hired"),
        ],
        default="applied"
    )
    applied_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.job.title} ({self.status})"
