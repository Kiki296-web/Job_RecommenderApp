from django.shortcuts import render
from .models import Job, JobRecommendation
from .serializers import JobSerializer, JobRecommendationSerializer
from rest_framework import generics, permissions

# --- Jobs ---
class JobListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)  # link job to logged-in user


class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# --- Recommendations ---
class JobRecommendationListView(generics.ListAPIView):
    serializer_class = JobRecommendationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return JobRecommendation.objects.filter(user=self.request.user)

