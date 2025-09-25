import django_filters
from api.models import Job


class JobFilter(django_filters.FilterSet):
    location = django_filters.CharFilter(field_name="location", lookup_expr="icontains")
    type = django_filters.ChoiceFilter(field_name="type", choices=Job.JOB_TYPE_CHOICES)
    location_type = django_filters.ChoiceFilter(
        field_name="location_type", choices=Job.LOCATION_TYPE_CHOICES
    )
    industry = django_filters.UUIDFilter(field_name="industry__id")
    salary_min = django_filters.NumberFilter(field_name="salary_min", lookup_expr="gte")
    salary_max = django_filters.NumberFilter(field_name="salary_max", lookup_expr="lte")

    class Meta:
        model = Job
        fields = [
            "location",
            "type",
            "location_type",
            "industry",
            "salary_min",
            "salary_max",
        ]
