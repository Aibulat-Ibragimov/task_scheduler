from django.db import models


class Task(models.Model):
    STATUS_CHOICES = (
        ('added', 'Добавлена'),
        ('in_progress', 'В работе'),
        ('completed', 'Выполнена'),
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
