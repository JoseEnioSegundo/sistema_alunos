from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Materia(models.Model):
    nome_materia = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    professor = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_materia


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    matricula = models.CharField(max_length=20, unique=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    data_nascimento = models.DateField()

    materias = models.ManyToManyField(Materia)

    def __str__(self):
        return self.nome