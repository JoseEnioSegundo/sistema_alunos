from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, Avg, Count
from django.db.models.functions import TruncDate
from django.http import JsonResponse
import json

from .models import Aluno, Materia, Nota, Curso
from .forms import AlunoForm, NotaForm, BuscaNotasForm


# ========== DASHBOARD ==========
def dashboard(request):
    """
    Página inicial do sistema com estatísticas gerais.
    Exibe totais de alunos, matérias, cursos e últimas notas lançadas.
    """
    total_alunos = Aluno.objects.filter(ativo=True).count()
    total_materias = Materia.objects.filter(ativo=True).count()
    total_cursos = Curso.objects.filter(ativo=True).count()
    total_notas = Nota.objects.count()
    
    # Últimas notas lançadas
    ultimas_notas = Nota.objects.select_related('aluno', 'materia').order_by('-data_avaliacao')[:5]
    
    # Alunos com melhor desempenho (média das notas)
    alunos_desempenho = Aluno.objects.annotate(
        media=Avg('notas__valor')
    ).filter(media__isnull=False).order_by('-media')[:5]
    
    contexto = {
        'total_alunos': total_alunos,
        'total_materias': total_materias,
        'total_cursos': total_cursos,
        'total_notas': total_notas,
        'ultimas_notas': ultimas_notas,
        'alunos_desempenho': alunos_desempenho,
    }
    
    return render(request, 'dashboard.html', contexto)


# ========== ALUNOS ==========
def lista_alunos(request):
    """
    Lista todos os alunos com opção de busca por nome, curso ou matrícula.
    Incluì paginação com 5 alunos por página.
    """
    buscar = request.GET.get('buscar')

    if buscar:
        # Busca por nome, curso ou matrícula (case-insensitive)
        alunos_lista = Aluno.objects.filter(
            Q(nome__icontains=buscar) |
            Q(curso__nome__icontains=buscar) |
            Q(matricula__icontains=buscar)
        ).order_by('-id')
    else:
        # Lista todos os alunos ativos
        alunos_lista = Aluno.objects.filter(ativo=True).order_by('-id')

    # Paginação: 5 alunos por página
    paginator = Paginator(alunos_lista, 5)
    page_number = request.GET.get('page')
    alunos = paginator.get_page(page_number)

    return render(request, 'alunos/lista_alunos.html', {'alunos': alunos})


def cadastrar_aluno(request):
    """
    Formulário para cadastrar um novo aluno.
    Valida dados e redireciona para a lista após sucesso.
    """
    if request.method == 'POST':
        form = AlunoForm(request.POST)

        if form.is_valid():
            aluno = form.save()
            messages.success(request, f'✓ Aluno {aluno.nome} cadastrado com sucesso!')
            return redirect('lista_alunos')
        else:
            messages.error(request, '✗ Erro ao cadastrar aluno. Verifique os dados.')

    else:
        form = AlunoForm()

    return render(request, 'alunos/cadastrar_aluno.html', {'form': form})


def editar_aluno(request, id):
    """
    Formulário para editar informações de um aluno existente.
    """
    aluno = get_object_or_404(Aluno, id=id)

    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)

        if form.is_valid():
            form.save()
            messages.success(request, f'✓ Aluno {aluno.nome} editado com sucesso!')
            return redirect('lista_alunos')
        else:
            messages.error(request, '✗ Erro ao editar aluno.')

    else:
        form = AlunoForm(instance=aluno)

    return render(request, 'alunos/editar_aluno.html', {'form': form, 'aluno': aluno})


def excluir_aluno(request, id):
    """
    Confirmação para exclusão de um aluno (exclusão lógica, marcar como inativo).
    """
    aluno = get_object_or_404(Aluno, id=id)

    if request.method == 'POST':
        # Exclusão lógica: marca como inativo em vez de deletar
        aluno.ativo = False
        aluno.save()
        messages.success(request, f'✓ Aluno {aluno.nome} desativado!')
        return redirect('lista_alunos')

    return render(request, 'alunos/confirmar_exclusao.html', {'aluno': aluno})


def perfil_aluno(request, id):
    """
    Exibe o perfil completo de um aluno com suas notas e médias.
    """
    aluno = get_object_or_404(Aluno, id=id)
    
    # Calcula média geral do aluno
    media_geral = Nota.objects.filter(aluno=aluno).aggregate(media=Avg('valor'))['media']
    
    # Agrupa notas por matéria
    notas_por_materia = []
    for materia in aluno.materias.all():
        notas = Nota.objects.filter(aluno=aluno, materia=materia)
        if notas.exists():
            media = notas.aggregate(media=Avg('valor'))['media']
            notas_por_materia.append({
                'materia': materia,
                'media': media,
                'total_avaliacoes': notas.count()
            })
    
    # Ordena por média (decrescente)
    notas_por_materia = sorted(notas_por_materia, key=lambda x: x['media'] if x['media'] else 0, reverse=True)
    
    # Últimas notas do aluno
    ultimas_notas = Nota.objects.filter(aluno=aluno).order_by('-data_avaliacao')[:10]
    
    contexto = {
        'aluno': aluno,
        'media_geral': media_geral,
        'notas_por_materia': notas_por_materia,
        'ultimas_notas': ultimas_notas,
    }
    
    return render(request, 'alunos/perfil_aluno.html', contexto)


# ========== MATÉRIAS ==========
def lista_materias(request):
    """
    Lista todas as matérias cadastradas no sistema.
    """
    materias = Materia.objects.filter(ativo=True).order_by('nome_materia')

    return render(request, 'alunos/lista_materias.html', {
        'materias': materias
    })


def gerenciar_materias(request, aluno_id):
    """
    Permite ao usuário adicionar/remover matérias de um aluno.
    Apenas matérias do mesmo curso são disponibilizadas.
    """
    aluno = get_object_or_404(Aluno, id=aluno_id)

    # Matérias disponíveis do curso do aluno
    materias = Materia.objects.filter(curso=aluno.curso).order_by('nome_materia')

    if request.method == "POST":
        # Atualiza as matérias selecionadas
        materias_ids = request.POST.getlist('materias')
        aluno.materias.set(materias_ids)

        messages.success(request, f'✓ Matérias de {aluno.nome} atualizadas com sucesso!')

        return redirect('gerenciar_materias', aluno_id=aluno.id)

    return render(request, 'alunos/gerenciar_materias.html', {
        'aluno': aluno,
        'materias': materias
    })


# ========== NOTAS ==========
def lista_notas(request):
    """
    Lista todas as notas do sistema com filtros opcionais.
    Permite buscar por aluno, matéria, tipo de avaliação e período.
    """
    form = BuscaNotasForm(request.GET)
    notas_lista = Nota.objects.select_related('aluno', 'materia').order_by('-data_avaliacao')
    
    # Aplica filtros se formulário foi submetido
    if request.GET:
        if form.is_valid():
            aluno = form.cleaned_data.get('aluno')
            materia = form.cleaned_data.get('materia')
            data_inicio = form.cleaned_data.get('data_inicio')
            data_fim = form.cleaned_data.get('data_fim')
            
            if aluno:
                notas_lista = notas_lista.filter(aluno=aluno)
            if materia:
                notas_lista = notas_lista.filter(materia=materia)
            if data_inicio:
                notas_lista = notas_lista.filter(data_avaliacao__gte=data_inicio)
            if data_fim:
                notas_lista = notas_lista.filter(data_avaliacao__lte=data_fim)
    
    # Paginação: 10 notas por página
    paginator = Paginator(notas_lista, 10)
    page_number = request.GET.get('page')
    notas = paginator.get_page(page_number)
    
    return render(request, 'alunos/lista_notas.html', {
        'notas': notas,
        'form': form,
    })


def lancar_nota(request):
    """
    Formulário para lançar uma nova nota para um aluno.
    Valida se o aluno está matriculado na matéria.
    """
    if request.method == 'POST':
        form = NotaForm(request.POST)
        
        if form.is_valid():
            # Valida se o aluno está matriculado na matéria
            aluno = form.cleaned_data['aluno']
            materia = form.cleaned_data['materia']
            
            if materia not in aluno.materias.all():
                messages.warning(request, '⚠ O aluno não está matriculado nesta matéria!')
                return redirect('lancar_nota')
            
            nota = form.save()
            messages.success(request, f'✓ Nota {nota.valor} lançada para {aluno.nome} em {materia.nome_materia}!')
            return redirect('lista_notas')
        else:
            messages.error(request, '✗ Erro ao lançar nota. Verifique os dados.')
    else:
        form = NotaForm()
    
    return render(request, 'alunos/lancar_nota.html', {'form': form})


def editar_nota(request, nota_id):
    """
    Edita uma nota já lançada.
    """
    nota = get_object_or_404(Nota, id=nota_id)
    
    if request.method == 'POST':
        form = NotaForm(request.POST, instance=nota)
        
        if form.is_valid():
            form.save()
            messages.success(request, f'✓ Nota atualizada para {nota.valor}!')
            return redirect('lista_notas')
        else:
            messages.error(request, '✗ Erro ao editar nota.')
    else:
        form = NotaForm(instance=nota)
    
    return render(request, 'alunos/editar_nota.html', {'form': form, 'nota': nota})


def excluir_nota(request, nota_id):
    """
    Confirmação para exclusão de uma nota.
    """
    nota = get_object_or_404(Nota, id=nota_id)
    
    if request.method == 'POST':
        aluno_nome = nota.aluno.nome
        materia_nome = nota.materia.nome_materia
        nota.delete()
        messages.success(request, f'✓ Nota de {aluno_nome} em {materia_nome} removida!')
        return redirect('lista_notas')
    
    return render(request, 'alunos/confirmar_exclusao_nota.html', {'nota': nota})


def boletim_aluno(request, aluno_id):
    """
    Exibe o boletim completo de um aluno com todas as suas notas
    agrupadas por matéria e médias.
    """
    aluno = get_object_or_404(Aluno, id=aluno_id)
    
    # Agrupa notas por matéria com cálculos
    notas_por_materia = []
    for materia in aluno.materias.all():
        notas = Nota.objects.filter(aluno=aluno, materia=materia).order_by('-data_avaliacao')
        if notas.exists():
            media = notas.aggregate(Avg('valor'))['valor__avg']
            notas_por_materia.append({
                'materia': materia,
                'notas': notas,
                'media': media,
                'status': 'Aprovado' if media >= 7 else 'Reprovado' if media < 5 else 'Recuperação'
            })
    
    # Média geral
    media_geral = Nota.objects.filter(aluno=aluno).aggregate(Avg('valor'))['valor__avg']
    
    contexto = {
        'aluno': aluno,
        'notas_por_materia': notas_por_materia,
        'media_geral': media_geral,
    }
    
    return render(request, 'alunos/boletim_aluno.html', contexto)