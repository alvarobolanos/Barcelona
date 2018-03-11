from django.db import models

# Create your models here.
class Agent(models.Model):
    name = models.CharField(max_length=40)
    title = models.CharField(max_length=100)
    hired_language = models.CharField(max_length=2)
    email = models.CharField(max_length=100)
    image = models.CharField(max_length=500)

    def __str__(self):
        return self.name
