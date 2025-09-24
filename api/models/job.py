from django.db import models
import uuid
from .industry import Industry
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Job(models.Model):
    JOB_TYPE_CHOICES = (
        ("internship", "Internship"),
        ("contract", "Contract"),
        ("full_time", "Full Time"),
        ("part_time", "Part Time"),
    )

    LOCATION_TYPE_CHOICES = (
        ("in-person", "In-Person"),
        ("remote", "Remote"),
        ("hybrid", "Hybrid"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = ArrayField(models.CharField(max_length=255))
    location_type = models.CharField(max_length=12, choices=LOCATION_TYPE_CHOICES)
    location = models.CharField(max_length=255)
    type = models.CharField(max_length=12, choices=JOB_TYPE_CHOICES)
    industry = models.ForeignKey(
        Industry, on_delete=models.CASCADE, related_name="applications"
    )
    salary_min = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    salary_max = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.company}"
