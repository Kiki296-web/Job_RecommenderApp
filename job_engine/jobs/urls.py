from django.urls import path
from .views import JobListCreateView, JobDetailView, JobRecommendationListView

urlpatterns = [
    path("", JobListCreateView.as_view(), name="job-list-create"),     
    path("<int:pk>/", JobDetailView.as_view(), name="job-detail"),     
    path("recommendations/", JobRecommendationListView.as_view(), name="job-recommendations"),
]
