from django.db import models
import uuid
from .job import Job
from .user import User


class Application(models.Model):
    APPLICATION_STATUS_CHOICES = (
        ("pending", "Pending"),
        ("reviewed", "Reviewed"),
        ("accepted", "Accepted"),
        ("rejected", "Rejected"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applications")
    applicant = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="applications"
    )
    cover_letter = models.TextField()
    resume = models.URLField()
    status = models.CharField(
        max_length=10, choices=APPLICATION_STATUS_CHOICES, default="pending"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("job", "applicant")
        ordering = ["-created_at"]

    def __str__(self):
        return (
            f"{self.applicant.first_name} {self.applicant.last_name} - {self.job.title}"
        )
