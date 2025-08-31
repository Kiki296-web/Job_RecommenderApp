from django.shortcuts import render,redirect
from rest_framework import generics, permissions
from .models import Application
from .serializers import ApplicationSerializer
from django.contrib.auth.decorators import login_required
from .models import Application
from jobs.models import Job


class ApplicationListCreateView(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ApplicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

@login_required
def apply_job(request, job_id):
    if request.method == "POST":
        job = Job.objects.get(id=job_id)
        Application.objects.get_or_create(user=request.user, job=job)  # avoid duplicates
    return redirect("dashboard")  # or wherever you want to go after applying