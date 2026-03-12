from django.contrib import admin
from .models import Aluno, Curso, Materia, Nota


# ========== Configuração do Admin para Curso ==========
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    """Admin customizado para Cursos"""
    list_display = ('nome', 'ativo', 'total_alunos')
    list_filter = ('ativo',)
    search_fields = ('nome',)
    list_editable = ('ativo',)

    def total_alunos(self, obj):
        """Exibe a quantidade de alunos do curso"""
        return obj.alunos.count()
    total_alunos.short_description = 'Total de Alunos'


# ========== Configuração do Admin para Matéria ==========
@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    """Admin customizado para Matérias"""
    list_display = ('nome_materia', 'professor', 'curso', 'carga_horaria', 'ativo')
    list_filter = ('curso', 'ativo')
    search_fields = ('nome_materia', 'professor')
    list_editable = ('ativo',)
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome_materia', 'professor', 'curso')
        }),
        ('Dados Acadêmicos', {
            'fields': ('carga_horaria',)
        }),
        ('Status', {
            'fields': ('ativo',)
        }),
    )


# ========== Configuração do Admin para Aluno ==========
@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    """Admin customizado para Alunos"""
    list_display = ('matricula', 'nome', 'curso', 'email', 'ativo')
    list_filter = ('curso', 'ativo', 'data_nascimento')
    search_fields = ('nome', 'matricula', 'email')
    list_editable = ('ativo',)
    
    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('nome', 'email', 'data_nascimento', 'idade')
        }),
        ('Informações Acadêmicas', {
            'fields': ('matricula', 'curso')
        }),
        ('Contato', {
            'fields': ('telefone', 'endereco')
        }),
        ('Matérias', {
            'fields': ('materias',)
        }),
        ('Status', {
            'fields': ('ativo',)
        }),
    )
    
    readonly_fields = ('idade',)

    def idade(self, obj):
        """Exibe a idade calculada do aluno"""
        return f"{obj.idade()} anos"
    idade.short_description = 'Idade'


# ========== Configuração do Admin para Nota ==========
@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    """Admin customizado para Notas"""
    list_display = ('aluno', 'materia', 'valor', 'tipo_avaliacao', 'data_avaliacao')
    list_filter = ('tipo_avaliacao', 'data_avaliacao', 'materia__curso')
    search_fields = ('aluno__nome', 'materia__nome_materia')
    date_hierarchy = 'data_avaliacao'
    
    fieldsets = (
        ('Aluno e Matéria', {
            'fields': ('aluno', 'materia')
        }),
        ('Avaliação', {
            'fields': ('valor', 'tipo_avaliacao')
        }),
        ('Detalhes', {
            'fields': ('data_avaliacao', 'observacao')
        }),
    )
    
    readonly_fields = ('data_avaliacao',)