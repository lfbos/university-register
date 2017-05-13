from django.db import models


class University(models.Model):
    name = models.CharField(max_length=128, verbose_name='university')

    def __str__(self):
        return self.name
