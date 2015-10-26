from django.db import models


class Photo(models.Model):
    image_file = models.ImageField()
    description = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)