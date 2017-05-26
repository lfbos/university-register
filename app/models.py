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
    courses = models.ManyToManyField(
        'Course',
        blank=True,
        related_name='students'
    )

    def __str__(self):
        return "{} - {}".format(
            self.get_full_name(),
            self.university
        )

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'


class Professor(mixins.BaseMixin):
    user = models.OneToOneField('auth.User', related_name='professor')
    profession = models.CharField(max_length=64, verbose_name='profession')
    university = models.ForeignKey('University', related_name='professors')
    dni = models.CharField(max_length=64, db_index=True, unique=True, verbose_name='professor ID')

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'professor'
        verbose_name_plural = 'professors'


class Course(mixins.BaseMixin):
    name = models.CharField(max_length=64, verbose_name='course')
    professor = models.ForeignKey('Professor', related_name='courses')

    def __str__(self):
        return "{} - {}".format(
            self.name,
            self.professor.university
        )

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'
