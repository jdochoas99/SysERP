from django.db import models


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    id_number = models.IntegerField(max_length=14)
    address = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
