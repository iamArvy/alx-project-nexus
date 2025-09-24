from rest_framework import viewsets, filters
from api.models import Job
from api.serializers import JobSerializer
from api.filters import JobFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from api.permissions import IsAdminOrReadOnly


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = JobFilter
    search_fields = ["title", "description", "requirements"]
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
