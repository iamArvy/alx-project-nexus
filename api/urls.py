# api/urls.py
from django.urls import path, include
from .views import (
    RegisterView,
    LoginView,
    RefreshTokenView,
    JobViewSet,
    IndustryViewSet,
    UserApplicationListView,
    JobApplicationListView,
    ApplicationViewSet,
)
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.authentication import JWTAuthentication

# Auth URLs
authUrlPatterns = [
    path("signup/", RegisterView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("refresh/", RefreshTokenView.as_view(), name="token_refresh"),
]

router = DefaultRouter()
router.register("jobs", JobViewSet, basename="job")
router.register("industries", IndustryViewSet, basename="industry")
router.register("applications", ApplicationViewSet, basename="application")


schema_view = get_schema_view(
    openapi.Info(
        title="Job Board Platform API",
        default_version="v1",
        description="""
            Welcome to my **Job Board Platform API** 👋

            This API allows admins to post jobs and manage applications, while applicants 
            can browse jobs and submit their applications.

            ---

            ### Authentication
            - Create an account at `/api/auth/signup`
            - Obtain a JWT token at `/api/auth/login/`
            - Refresh your token at `/api/auth/token/refresh/`
            - Add it to requests as:  
            `Authorization: Bearer <your_token>`

            ---

            ### Endpoints

            #### Jobs
            - **List all jobs** → `GET /api/jobs/`
            - **Retrieve a job** → `GET /api/jobs/{id}/`
            - **Create a job** (Admin only) → `POST /api/jobs/`
            - **Update/Delete a job** (Admin only) → `PUT/PATCH/DELETE /api/jobs/{id}/`

            #### Applications
            - **List applications for a job** (Admin only) → `GET /api/jobs/{job_pk}/applications/`
            - **List my applications** (User only) → `GET /api/user/applications/`
            - **Create application** (User only) → `POST /api/applications/`
            - **Retrieve application** (User or Admin) → `GET /api/applications/{id}/`
            - **Change application status** (Admin only) → `PATCH /api/applications/{id}/change_status/`

            #### Industries
            - **List industries** → `GET /api/industries/`
            - **Retrieve industry** → `GET /api/industries/{id}/`
            - **Create industry** (Admin only) → `POST /api/industries/`
            - **Update/Delete industry** (Admin only) → `PUT/PATCH/DELETE /api/industries/{id}/`
            ---

            ### Notes
            - Applicants can only apply once per job (`job + applicant` is unique).
            - Recruiters can only see applications for jobs they posted.
            - Statuses for applications: `pending`, `reviewed`, `accepted`, `rejected`.
            - Jobs support filtering and search by title, industry, location, and type.
            """,
        contact=openapi.Contact(
            name="Oluwaseyi Oke",
            url="https://iamarvy.netlify.app",
            email="okeseyi5@gmail.com",
        ),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=(JWTAuthentication,),
)
# Main Urls
urlpatterns = [
    path("auth/", include(authUrlPatterns)),
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("", include(router.urls)),
    path(
        "user/applications/",
        UserApplicationListView.as_view(),
        name="user-applications",
    ),
    path(
        "jobs/<uuid:id>/applications/",
        JobApplicationListView.as_view(),
        name="job-applications",
    ),
]
