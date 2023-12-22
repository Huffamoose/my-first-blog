from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )  # ForeignKey is a link to another model
    title = models.CharField(
        max_length=200
    )  # CharField is for text with a limited number of characters
    text = models.TextField()  # TextField is for long text without a limit
    created_date = models.DateTimeField(
        default=timezone.now
    )  # DateTimeField is for date and time
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):  # method
        self.published_date = timezone.now()
        self.save()

    def __str__(self):  # dunder method
        return self.title
