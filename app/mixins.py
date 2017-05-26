import uuid

from django.db import models


class BaseMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Person(BaseMixin, models.Model):
    first_name = models.CharField(max_length=64, verbose_name='first name')
    last_name = models.CharField(max_length=64, verbose_name='last name')

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return "{} {}".format(
            self.first_name,
            self.last_name
        )

    class Meta:
        abstract = True
