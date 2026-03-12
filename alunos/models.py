from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Curso(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True, null=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'


class Materia(models.Model):
    nome_materia = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='materias')
    professor = models.CharField(max_length=100)
    carga_horaria = models.PositiveIntegerField(default=60, help_text="Carga horária em horas")
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome_materia} - {self.professor}"

    class Meta:
        verbose_name = 'Matéria'
        verbose_name_plural = 'Matérias'
        unique_together = ['nome_materia', 'curso']


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    matricula = models.CharField(max_length=20, unique=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='alunos')
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=15, blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    ativo = models.BooleanField(default=True)

    materias = models.ManyToManyField(Materia, related_name='alunos_matriculados', blank=True)

    def __str__(self):
        return f"{self.nome} - {self.matricula}"

    def idade(self):
        from datetime import date
        hoje = date.today()
        return hoje.year - self.data_nascimento.year - ((hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day))

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'


class Nota(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='notas')
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='notas')
    valor = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        help_text="Nota de 0.00 a 10.00"
    )
    data_avaliacao = models.DateField(auto_now_add=True)
    tipo_avaliacao = models.CharField(
        max_length=20,
        choices=[
            ('PROVA', 'Prova'),
            ('TRABALHO', 'Trabalho'),
            ('ATIVIDADE', 'Atividade'),
            ('EXERCICIO', 'Exercício'),
            ('PROJETO', 'Projeto'),
        ],
        default='PROVA'
    )
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.aluno.nome} - {self.materia.nome_materia}: {self.valor}"

    class Meta:
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'
        unique_together = ['aluno', 'materia', 'data_avaliacao', 'tipo_avaliacao']
        ordering = ['-data_avaliacao']