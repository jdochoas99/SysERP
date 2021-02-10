from django.contrib.auth.models import User
from django.db import models
from apps.clients.models import Client
from apps.companies.models import Company
# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    client = models.ForeignKey(Client, on_delete=models.PROTECT, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=False, blank=False)
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
