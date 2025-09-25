from rest_framework import viewsets, filters
from api.models import Job
from api.serializers import JobSerializer
from api.filters import JobFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from api.permissions import IsAdminOrReadOnly
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework_extensions.cache.decorators import cache_response
from api.cache_keys import JobsListKeyConstructor, JobsDetailKeyConstructor
from drf_yasg.utils import swagger_auto_schema
from api.swagger_params import job_filter_params


class JobViewSet(CacheResponseMixin, viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = JobFilter
    search_fields = ["title", "description"]
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    cache_response_key_func = JobsListKeyConstructor()

    @cache_response(key_func=JobsDetailKeyConstructor(), timeout=60 * 5)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(manual_parameters=job_filter_params)
    @cache_response(key_func=JobsListKeyConstructor(), timeout=60 * 10)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
