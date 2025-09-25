from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from api.models import Application
from api.cache_keys import (
    ApplicationsDetailKeyConstructor,
    ApplicationsListKeyConstructor,
    UserApplicationsListKeyConstructor,
)


@receiver([post_save, post_delete], sender=Application)
def clear_application_cache(sender, instance, **kwargs):
    """
    Invalidate cache whenever an Application is created, updated, or deleted.
    """

    request = None  # no real request here, but some key constructors need this

    # ✅ Clear detail cache for this application
    ApplicationsDetailKeyConstructor().invalidate_cache(
        view_instance=None,
        view_method="retrieve",
        request=request,
        args=[],
        kwargs={"pk": instance.pk},
    )

    # ✅ Clear all list caches
    ApplicationsListKeyConstructor().invalidate_cache(
        view_instance=None, view_method=None, request=request, args=[], kwargs={}
    )
    UserApplicationsListKeyConstructor().invalidate_cache(
        view_instance=None, view_method=None, request=request, args=[], kwargs={}
    )
