# editor/models.py
from django.db import models

class XmlData(models.Model):
    data = models.TextField()

    def __str__(self):
        return self.data[:50]  # Return first 50 characters for display
