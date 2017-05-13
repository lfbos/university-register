from django.db import models

from app import mixins


class University(mixins.BaseMixin):
    name = models.CharField(max_length=128, verbose_name='university')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'university'
        verbose_name_plural = 'universities'


class Student(mixins.Person):
    university = models.ForeignKey('University', related_name='students')

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'


class Professor(mixins.Person):
    profession = models.CharField(max_length=64, verbose_name='profession')
    university = models.ForeignKey('University', related_name='professors')

    class Meta:
        verbose_name = 'professor'
        verbose_name_plural = 'professors'
