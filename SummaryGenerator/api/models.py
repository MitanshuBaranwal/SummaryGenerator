
# Create your models here.
from django.db import models

class TextData(models.Model):
    original_text = models.TextField()
    summary = models.TextField(blank=True, null=True)
    bullet_points = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"TextData {self.id}"