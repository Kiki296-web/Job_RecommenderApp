from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from users.models import User
from jobs.models import Job

class JobAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )
        self.job = Job.objects.create(
            title="Backend Developer",
            description="Work on APIs",
            required_skills="Python, Django, REST",
            category="Software",
            location="Remote",
            posted_by=self.user,
        )

    def test_list_jobs(self):
        url = reverse("job-list-create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_job(self):
        self.client.login(username="testuser", password="testpass123")
        url = reverse("job-list-create")
        data = {
            "title": "Frontend Developer",
            "description": "Work on UI",
            "required_skills": "React, CSS",
            "category": "Software",
            "location": "Cape Town"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "Frontend Developer")

    def test_retrieve_job(self):
        url = reverse("job-detail", kwargs={"pk": self.job.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Backend Developer")

    def test_update_job(self):
        self.client.login(username="testuser", password="testpass123")
        url = reverse("job-detail", kwargs={"pk": self.job.id})
        data = {"title": "Updated Job Title"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Job Title")

    def test_delete_job(self):
        self.client.login(username="testuser", password="testpass123")
        url = reverse("job-detail", kwargs={"pk": self.job.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Job.objects.filter(id=self.job.id).exists())
