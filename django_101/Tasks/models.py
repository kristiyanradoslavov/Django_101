from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=80, null=False)
    priority = models.IntegerField(null=False)
