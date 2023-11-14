from django.db import models

# Create your models here.

class Comments(models.Model):
    comment = models.TextField()

    def __str__(self):
        return self.comment
