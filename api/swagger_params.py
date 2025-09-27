from drf_yasg import openapi

# Filter Parameters for Jobs
job_filter_params = [
    openapi.Parameter(
        "location",
        openapi.IN_QUERY,
        description="Filter by location",
        type=openapi.TYPE_STRING,
    ),
    openapi.Parameter(
        "type",
        openapi.IN_QUERY,
        description="Filter by job type",
        type=openapi.TYPE_STRING,
    ),
    openapi.Parameter(
        "location_type",
        openapi.IN_QUERY,
        description="Filter by location type",
        type=openapi.TYPE_STRING,
    ),
    openapi.Parameter(
        "industry",
        openapi.IN_QUERY,
        description="Filter by industry",
        type=openapi.TYPE_STRING,
    ),
    openapi.Parameter(
        "salary_min",
        openapi.IN_QUERY,
        description="Filter by min salary",
        type=openapi.TYPE_STRING,
    ),
    openapi.Parameter(
        "salary_max",
        openapi.IN_QUERY,
        description="Filter by max salary",
        type=openapi.TYPE_STRING,
    ),
]


# Filter Parameters for Applications
application_filter_params = [
    openapi.Parameter(
        "status",
        openapi.IN_QUERY,
        description="Filter by status",
        type=openapi.TYPE_STRING,
    ),
]
