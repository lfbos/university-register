from django.db import models


class University(models.Model):
    name = models.CharField(max_length=128, verbose_name='university')

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=64, verbose_name='first name')
    last_name = models.CharField(max_length=64, verbose_name='last name')
    dni = models.CharField(max_length=64, verbose_name='student ID')
    university = models.ForeignKey('University', related_name='students')

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return "{} {}".format(
            self.first_name,
            self.last_name
        )
