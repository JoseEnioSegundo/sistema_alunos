from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    matricula = models.CharField(max_length=20)
    curso = models.CharField(max_length=100)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome