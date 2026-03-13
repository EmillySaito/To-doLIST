from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):

    TYPE_CHOICES = [
        ('estudo', 'Estudo'),
        ('trabalho', 'Trabalho'),
        ('pessoal', 'Pessoal'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    nome = models.CharField(max_length=200)

    tipo = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES
    )

    data_conclusao = models.DateField()

    concluida = models.BooleanField(default=False)

    def __str__(self):
        return self.nome