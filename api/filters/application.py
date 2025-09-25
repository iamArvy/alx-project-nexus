import django_filters
from api.models import Application


class ApplicationFilter(django_filters.FilterSet):
    job = django_filters.UUIDFilter(field_name="job__id")
    applicant = django_filters.UUIDFilter(field_name="applicant__id")
    status = django_filters.ChoiceFilter(
        field_name="status", choices=Application.APPLICATION_STATUS_CHOICES
    )

    class Meta:
        model = Application
        fields = [
            "status",
        ]
