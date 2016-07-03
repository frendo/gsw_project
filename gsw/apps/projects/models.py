from django.db import models
from django.utils import timezone


class Project(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    company_logo = models.ImageField()
    text = models.TextField()
    completed_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.completed_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
