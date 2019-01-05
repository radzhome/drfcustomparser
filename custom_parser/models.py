from django.db import models


class Video(models.Model):
    """
    Video class
    """
    version = models.TextField(null=False, blank=False, default="1.0")

    class Meta:
        db_table = 'videos'
