from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_alunos, name='lista_alunos'),
    path('cadastrar/', views.cadastrar_aluno, name='cadastrar_aluno'),
    path('excluir/<int:id>/', views.excluir_aluno, name='excluir_aluno'),
    path('editar/<int:id>/', views.editar_aluno, name='editar_aluno'),
    path('materias/', views.lista_materias, name='lista_materias'),
    path('aluno/<int:aluno_id>/materias/', views.gerenciar_materias, name='gerenciar_materias'),    
]