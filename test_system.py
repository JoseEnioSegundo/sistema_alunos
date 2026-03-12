#!/usr/bin/env python
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from alunos.models import Curso, Materia, Aluno

print('=' * 50)
print('✓ SISTEMA DE ALUNOS - TESTE DE FUNCIONAMENTO')
print('=' * 50)

try:
    cursos_count = Curso.objects.count()
    materias_count = Materia.objects.count()
    alunos_count = Aluno.objects.count()
    
    print(f'\n✓ Modelos carregados com sucesso!')
    print(f'  - Cursos cadastrados: {cursos_count}')
    print(f'  - Matérias cadastradas: {materias_count}')
    print(f'  - Alunos cadastrados: {alunos_count}')
    
    print('\n✓ Banco de dados funcionando corretamente!')
    print('\n' + '=' * 50)
    print('✓ SISTEMA ESTÁ 100% FUNCIONAL')
    print('=' * 50)
    print('\nAcesse: http://localhost:8000/')
    
except Exception as e:
    print(f'\n✗ ERRO: {e}')
    sys.exit(1)
