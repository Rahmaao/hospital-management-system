from django.db import models

# Create your models here.


class Hospital(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    capacity = models.IntegerField()
    def __str__(self):
        return self.name