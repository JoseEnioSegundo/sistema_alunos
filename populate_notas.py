#!/usr/bin/env python
"""
Script para popular o banco de dados com notas de teste.
Adiciona notas realistas para demonstrar as funcionalidades do sistema.
"""

import os
import sys
import django
from datetime import date, timedelta
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from alunos.models import Aluno, Nota

def criar_notas_teste():
    """
    Cria notas fictícias para alunos e matérias.
    Simula um semestre completo com provas, trabalhos e exercícios.
    """
    alunos = Aluno.objects.filter(ativo=True)[:20]  # Primeiros 20 alunos
    tipos_avaliacao = ['PROVA', 'TRABALHO', 'ATIVIDADE', 'EXERCICIO', 'PROJETO']
    
    contador = 0
    
    for aluno in alunos:
        # Para cada matéria do aluno
        for materia in aluno.materias.all()[:3]:  # Apenas 3 matérias por teste
            # Criar 3-5 avaliações por matéria
            num_avaliacoes = random.randint(3, 5)
            
            for i in range(num_avaliacoes):
                # Data aleatória nos últimos 60 dias, garantindo datas diferentes
                dias_atras = random.randint(0, 60 - i) 
                data_avaliacao = date.today() - timedelta(days=dias_atras)
                
                # Nota aleatória de 4.0 a 10.0 (mais realista)
                nota_valor = round(random.uniform(4.0, 10.0), 2)
                
                # Tipo de avaliação aleatório
                tipo_aval = random.choice(tipos_avaliacao)
                
                try:
                    # Cria a nota
                    nota = Nota.objects.create(
                        aluno=aluno,
                        materia=materia,
                        valor=nota_valor,
                        data_avaliacao=data_avaliacao,
                        tipo_avaliacao=tipo_aval,
                        observacao=f"Avaliação de {tipo_aval.lower()} - {i+1}ª prova"
                    )
                    
                    contador += 1
                    print(f"✓ Nota #{contador}: {aluno.nome} - {materia.nome_materia} - {nota_valor} ({tipo_aval})")
                
                except Exception as e:
                    # Ignora duplicatas
                    pass
    
    return contador

def main():
    print("=" * 70)
    print("🎓 SISTEMA DE ALUNOS - POPULANDO NOTAS DE TESTE")
    print("=" * 70)
    
    try:
        print("\n📝 Criando notas de teste...\n")
        total_notas = criar_notas_teste()
        
        print("\n" + "=" * 70)
        print(f"✅ SUCESSO! {total_notas} notas foram criadas!")
        print("=" * 70)
        print("\nAgora você pode:")
        print("  • Ver o dashboard com estatísticas")
        print("  • Consultar o boletim de alunos")
        print("  • Visualizar gráficos de desempenho")
        print("  • Filtrar notas por aluno/matéria")
        print("\n🚀 Acesse: http://localhost:8000/")
        
    except Exception as e:
        print(f"\n❌ ERRO: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()