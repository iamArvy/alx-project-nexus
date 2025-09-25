from rest_framework import viewsets, mixins, filters
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from api.models import Application
from api.serializers import ApplicationSerializer, ApplicationStatusSerializer
from api.filters import ApplicationFilter
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from api.permissions import IsAdmin, IsUser, IsAdminOrIsApplicationOwner
from rest_framework.permissions import IsAuthenticated
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from api.cache_keys import (
    ApplicationsListKeyConstructor,
    ApplicationsDetailKeyConstructor,
    UserApplicationsListKeyConstructor,
)
from rest_framework_extensions.cache.decorators import cache_response
from drf_yasg.utils import swagger_auto_schema
from api.swagger_params import application_filter_params


class ApplicationViewSet(
    mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    """
    Supports:
    - creating a new application
    - retrieving a single application
    - changing the status of an application
    """

    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def get_serializer_class(self):
        if self.action == "change_status":
            return ApplicationStatusSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [IsUser]
        elif self.action == "retrieve":
            permission_classes = [IsAdminOrIsApplicationOwner]
        elif self.action == "change_status":
            permission_classes = [IsAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)

    @cache_response(key_func=ApplicationsDetailKeyConstructor(), timeout=60 * 5)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @action(
        detail=True,
        methods=["patch"],
        url_path="change_status",
        permission_classes=[IsAdmin],
    )
    def change_status(self, request, pk=None):
        application = self.get_object()
        new_status = request.data.get("status")

        if new_status not in dict(Application.APPLICATION_STATUS_CHOICES):
            return Response({"error": "Invalid status"}, status=400)

        application.status = new_status
        application.save()

        return Response({"status": "updated", "new_status": application.status})


class JobApplicationListView(CacheResponseMixin, ListAPIView):
    """
    Recruiter can only list applications for their own jobs
    at /jobs/{id}/applications/
    """

    permission_classes = [IsAdmin]
    serializer_class = ApplicationSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = ApplicationFilter
    search_fields = [
        "applicant__first_name",
        "applicant__last_name",
    ]
    cache_response_key_func = ApplicationsListKeyConstructor()

    def get_queryset(self):
        job_id = self.kwargs.get("id")
        return Application.objects.filter(job_id=job_id)

    @swagger_auto_schema(manual_parameters=application_filter_params)
    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class UserApplicationListView(CacheResponseMixin, ListAPIView):
    """
    Applicant can only list their own applications
    at /user/applications/
    """

    permission_classes = [IsUser]
    serializer_class = ApplicationSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = ApplicationFilter
    search_fields = ["job__title"]
    cache_response_key_func = UserApplicationsListKeyConstructor()

    def get_queryset(self):
        return Application.objects.filter(applicant=self.request.user)

    @swagger_auto_schema(manual_parameters=application_filter_params)
    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
