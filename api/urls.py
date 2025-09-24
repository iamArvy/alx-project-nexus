# api/urls.py
from django.urls import path, include
from rest_framework_nested.routers import NestedDefaultRouter
from .views import (
    RegisterView,
    LoginView,
    RefreshTokenView,
    JobViewSet,
    IndustryViewSet,
    UserApplicationViewSet,
    JobApplicationViewSet,
    ApplicationViewSet,
)
from rest_framework.routers import DefaultRouter

# Auth URLs
authUrlPatterns = [
    path("signup/", RegisterView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("refresh/", RefreshTokenView.as_view(), name="token_refresh"),
]

router = DefaultRouter()
router.register("jobs", JobViewSet, basename="job")
router.register("industries", IndustryViewSet, basename="industry")
router.register(
    "user/applications",
    UserApplicationViewSet,
    basename="user-application",
)
router.register("applications", ApplicationViewSet, basename="application")
jobs_router = NestedDefaultRouter(router, r"jobs", lookup="job")
jobs_router.register(
    r"applications", JobApplicationViewSet, basename="job-applications"
)

# Main Urls
urlpatterns = [
    path("auth/", include(authUrlPatterns)),
    path("", include(router.urls + jobs_router.urls)),
]
