#!/usr/bin/env python
import os
import sys
import django
from datetime import date, timedelta
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from alunos.models import Curso, Materia, Aluno

def criar_cursos():
    """Cria cursos fictícios"""
    cursos = [
        "Engenharia de Software",
        "Ciência da Computação",
        "Sistemas de Informação",
        "Análise e Desenvolvimento de Sistemas",
        "Engenharia da Computação",
        "Tecnologia em Jogos Digitais",
        "Redes de Computadores",
        "Segurança da Informação"
    ]

    cursos_criados = []
    for nome_curso in cursos:
        curso, criado = Curso.objects.get_or_create(nome=nome_curso)
        cursos_criados.append(curso)
        if criado:
            print(f"✓ Criado curso: {nome_curso}")
        else:
            print(f"✓ Já existe curso: {nome_curso}")

    return cursos_criados

def criar_materias(cursos):
    """Cria matérias fictícias associadas aos cursos"""
    materias_data = [
        # Engenharia de Software
        ("Programação Orientada a Objetos", "Prof. Dr. Carlos Silva"),
        ("Engenharia de Requisitos", "Profª. Dra. Ana Santos"),
        ("Arquitetura de Software", "Prof. Dr. Roberto Oliveira"),
        ("Testes de Software", "Profª. Dra. Maria Fernandes"),
        ("DevOps e CI/CD", "Prof. Dr. João Pereira"),

        # Ciência da Computação
        ("Algoritmos e Estruturas de Dados", "Prof. Dr. Pedro Costa"),
        ("Teoria da Computação", "Profª. Dra. Luciana Almeida"),
        ("Inteligência Artificial", "Prof. Dr. Marcos Rodrigues"),
        ("Banco de Dados", "Profª. Dra. Juliana Lima"),
        ("Redes Neurais", "Prof. Dr. Fernando Souza"),

        # Sistemas de Informação
        ("Gestão de Projetos", "Prof. Dr. Ricardo Mendes"),
        ("Sistemas Operacionais", "Profª. Dra. Patrícia Gomes"),
        ("Análise de Sistemas", "Prof. Dr. André Santos"),
        ("Segurança de Sistemas", "Profª. Dra. Carla Oliveira"),
        ("Business Intelligence", "Prof. Dr. Eduardo Silva"),

        # Análise e Desenvolvimento de Sistemas
        ("Lógica de Programação", "Prof. Dr. Gabriel Costa"),
        ("Desenvolvimento Web", "Profª. Dra. Helena Pereira"),
        ("Mobile Development", "Prof. Dr. Lucas Almeida"),
        ("Qualidade de Software", "Profª. Dra. Sofia Rodrigues"),
        ("Metodologias Ágeis", "Prof. Dr. Thiago Lima"),

        # Engenharia da Computação
        ("Circuitos Digitais", "Prof. Dr. Bruno Fernandes"),
        ("Microprocessadores", "Profª. Dra. Daniela Souza"),
        ("Sistemas Embarcados", "Prof. Dr. Rafael Costa"),
        ("Eletrônica Digital", "Profª. Dra. Amanda Santos"),
        ("Controle e Automação", "Prof. Dr. Vinícius Oliveira"),

        # Tecnologia em Jogos Digitais
        ("Game Design", "Prof. Dr. Leonardo Pereira"),
        ("Programação de Jogos", "Profª. Dra. Isabela Almeida"),
        ("Computação Gráfica", "Prof. Dr. Diego Rodrigues"),
        ("Áudio em Jogos", "Profª. Dra. Carolina Lima"),
        ("Realidade Virtual", "Prof. Dr. Gustavo Silva"),

        # Redes de Computadores
        ("Redes TCP/IP", "Prof. Dr. Marcelo Costa"),
        ("Administração de Redes", "Profª. Dra. Vanessa Oliveira"),
        ("Segurança de Redes", "Prof. Dr. Alexandre Santos"),
        ("Cloud Computing", "Profª. Dra. Renata Fernandes"),
        ("IoT e Redes Industriais", "Prof. Dr. Felipe Almeida"),

        # Segurança da Informação
        ("Criptografia", "Prof. Dr. Rogério Pereira"),
        ("Ethical Hacking", "Profª. Dra. Tatiana Rodrigues"),
        ("Auditoria de Sistemas", "Prof. Dr. Sérgio Lima"),
        ("Governança de TI", "Profª. Dra. Letícia Souza"),
        ("Forense Digital", "Prof. Dr. Paulo Costa")
    ]

    materias_criadas = []
    for i, (nome_materia, professor) in enumerate(materias_data):
        curso = cursos[i % len(cursos)]  # Distribui matérias entre cursos
        materia, criado = Materia.objects.get_or_create(
            nome_materia=nome_materia,
            curso=curso,
            defaults={'professor': professor}
        )
        materias_criadas.append(materia)
        if criado:
            print(f"✓ Criada matéria: {nome_materia} ({curso.nome})")
        else:
            print(f"✓ Já existe matéria: {nome_materia}")

    return materias_criadas

def criar_alunos(cursos):
    """Cria alunos fictícios"""
    nomes = [
        "João Silva", "Maria Santos", "Pedro Oliveira", "Ana Costa", "Lucas Pereira",
        "Julia Almeida", "Gabriel Rodrigues", "Beatriz Lima", "Rafael Souza", "Carolina Fernandes",
        "Thiago Mendes", "Isabela Gomes", "Felipe Santos", "Amanda Oliveira", "Bruno Costa",
        "Larissa Pereira", "Diego Almeida", "Camila Rodrigues", "Vinícius Lima", "Natália Souza",
        "Matheus Fernandes", "Letícia Mendes", "Gustavo Gomes", "Sofia Santos", "Leonardo Oliveira",
        "Manuela Costa", "Enzo Pereira", "Valentina Almeida", "Arthur Rodrigues", "Helena Lima",
        "Miguel Souza", "Alice Fernandes", "Davi Mendes", "Laura Gomes", "Bernardo Santos",
        "Sophia Oliveira", "Heitor Costa", "Isabella Pereira", "Samuel Almeida", "Clara Rodrigues",
        "Benjamin Lima", "Luiza Souza", "Joaquim Fernandes", "Cecília Mendes", "Lorenzo Gomes"
    ]

    emails = [
        "joao.silva@email.com", "maria.santos@email.com", "pedro.oliveira@email.com",
        "ana.costa@email.com", "lucas.pereira@email.com", "julia.almeida@email.com",
        "gabriel.rodrigues@email.com", "beatriz.lima@email.com", "rafael.souza@email.com",
        "carolina.fernandes@email.com", "thiago.mendes@email.com", "isabela.gomes@email.com",
        "felipe.santos@email.com", "amanda.oliveira@email.com", "bruno.costa@email.com",
        "larissa.pereira@email.com", "diego.almeida@email.com", "camila.rodrigues@email.com",
        "vinicius.lima@email.com", "natalia.souza@email.com", "matheus.fernandes@email.com",
        "leticia.mendes@email.com", "gustavo.gomes@email.com", "sofia.santos@email.com",
        "leonardo.oliveira@email.com", "manuela.costa@email.com", "enzo.pereira@email.com",
        "valentina.almeida@email.com", "arthur.rodrigues@email.com", "helena.lima@email.com",
        "miguel.souza@email.com", "alice.fernandes@email.com", "davi.mendes@email.com",
        "laura.gomes@email.com", "bernardo.santos@email.com", "sophia.oliveira@email.com",
        "heitor.costa@email.com", "isabella.pereira@email.com", "samuel.almeida@email.com",
        "clara.rodrigues@email.com", "benjamin.lima@email.com", "luiza.souza@email.com",
        "joaquim.fernandes@email.com", "cecilia.mendes@email.com", "lorenzo.gomes@email.com"
    ]

    alunos_criados = []
    for i, (nome, email) in enumerate(zip(nomes, emails)):
        # Gera matrícula única
        matricula = f"2024{random.randint(10000, 99999)}{i:02d}"

        # Data de nascimento aleatória (18-25 anos)
        hoje = date.today()
        idade = random.randint(18, 25)
        nascimento = hoje - timedelta(days=idade*365 + random.randint(0, 364))

        # Seleciona curso aleatório
        curso = random.choice(cursos)

        aluno, criado = Aluno.objects.get_or_create(
            matricula=matricula,
            defaults={
                'nome': nome,
                'email': email,
                'curso': curso,
                'data_nascimento': nascimento
            }
        )

        alunos_criados.append(aluno)
        if criado:
            print(f"✓ Criado aluno: {nome} (Matrícula: {matricula})")
        else:
            print(f"✓ Já existe aluno: {nome}")

    return alunos_criados

def associar_materias_alunos(alunos):
    """Associa matérias aleatórias aos alunos"""
    from alunos.models import Materia

    for aluno in alunos:
        # Busca matérias do curso do aluno
        materias_curso = list(Materia.objects.filter(curso=aluno.curso))

        if materias_curso:
            # Seleciona 3-6 matérias aleatoriamente
            num_materias = random.randint(3, min(6, len(materias_curso)))
            materias_selecionadas = random.sample(materias_curso, num_materias)

            # Associa as matérias ao aluno
            aluno.materias.set(materias_selecionadas)
            print(f"✓ Associadas {len(materias_selecionadas)} matérias ao aluno {aluno.nome}")

def main():
    print("=" * 60)
    print("🎓 SISTEMA DE ALUNOS - POPULANDO BANCO COM DADOS FICTÍCIOS")
    print("=" * 60)

    try:
        print("\n📚 CRIANDO CURSOS...")
        cursos = criar_cursos()

        print("\n📖 CRIANDO MATÉRIAS...")
        materias = criar_materias(cursos)

        print("\n👨‍🎓 CRIANDO ALUNOS...")
        alunos = criar_alunos(cursos)

        print("\n🔗 ASSOCIANDO MATÉRIAS AOS ALUNOS...")
        associar_materias_alunos(alunos)

        print("\n" + "=" * 60)
        print("✅ BANCO POPULADO COM SUCESSO!")
        print("=" * 60)
        print(f"📊 RESUMO:")
        print(f"   • Cursos: {len(cursos)}")
        print(f"   • Matérias: {len(materias)}")
        print(f"   • Alunos: {len(alunos)}")
        print("\n🚀 Sistema pronto para uso!")
        print("   Acesse: http://localhost:8000/")

    except Exception as e:
        print(f"\n❌ ERRO: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()