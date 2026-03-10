from django.contrib import admin
from .models import Aluno, Curso, Materia

admin.site.register(Aluno)
admin.site.register(Curso)
admin.site.register(Materia)