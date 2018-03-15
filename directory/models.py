from django.db import models
from django.utils.text import slugify

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=100)
    image = models.CharField(max_length=500)
    slug = models.SlugField(max_length=40, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)
        super(Employee, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
