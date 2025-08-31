from django.urls import path
from .views import ApplicationListCreateView, ApplicationDetailView,apply_job

urlpatterns = [
    path("applications/", ApplicationListCreateView.as_view(), name="application-list-create"),
    path("applications/<int:pk>/", ApplicationDetailView.as_view(), name="application-detail"),
    path("apply/<int:job_id>/", apply_job, name="apply_job"),
]
