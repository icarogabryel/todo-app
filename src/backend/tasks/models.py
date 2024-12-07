from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=200)
    cel_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'
        db_table = 'person'
