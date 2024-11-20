from django.db import models


# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=222)
    email = models.CharField(max_length=222)
    message = models.TextField()

    def __str__(self):
        return self.name
