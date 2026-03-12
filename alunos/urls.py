from django.urls import path
from . import views

# ========== ROTAS DO SISTEMA DE ALUNOS ==========

urlpatterns = [
    # Dashboard e página inicial
    path('', views.dashboard, name='dashboard'),
    
    # Alunos
    path('alunos/', views.lista_alunos, name='lista_alunos'),
    path('alunos/cadastrar/', views.cadastrar_aluno, name='cadastrar_aluno'),
    path('alunos/<int:id>/editar/', views.editar_aluno, name='editar_aluno'),
    path('alunos/<int:id>/excluir/', views.excluir_aluno, name='excluir_aluno'),
    path('alunos/<int:id>/perfil/', views.perfil_aluno, name='perfil_aluno'),
    path('alunos/<int:aluno_id>/materias/', views.gerenciar_materias, name='gerenciar_materias'),
    path('alunos/<int:aluno_id>/boletim/', views.boletim_aluno, name='boletim_aluno'),
    
    # Matérias
    path('materias/', views.lista_materias, name='lista_materias'),
    
    # Notas
    path('notas/', views.lista_notas, name='lista_notas'),
    path('notas/lancar/', views.lancar_nota, name='lancar_nota'),
    path('notas/<int:nota_id>/editar/', views.editar_nota, name='editar_nota'),
    path('notas/<int:nota_id>/excluir/', views.excluir_nota, name='excluir_nota'),
]