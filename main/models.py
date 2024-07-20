from django.db import models


class Task(models.Model):
    title = models.CharField('Name', max_length=20)
    description = models.TextField('Descriprion')

    def __str__(self):
        return self.title