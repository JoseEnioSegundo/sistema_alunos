from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Aluno, Materia
from .forms import AlunoForm


def lista_alunos(request):
    buscar = request.GET.get('buscar')

    if buscar:
        alunos_lista = Aluno.objects.filter(
            Q(nome__icontains=buscar) |
            Q(curso__nome__icontains=buscar) |
            Q(matricula__icontains=buscar)
        ).order_by('-id')
    else:
        alunos_lista = Aluno.objects.all().order_by('-id')

    paginator = Paginator(alunos_lista, 5)
    page_number = request.GET.get('page')
    alunos = paginator.get_page(page_number)

    return render(request, 'alunos/lista_alunos.html', {'alunos': alunos})


def cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Aluno cadastrado com sucesso!')
            return redirect('lista_alunos')

    else:
        form = AlunoForm()

    return render(request, 'alunos/cadastrar_aluno.html', {'form': form})


def editar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)

    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)

        if form.is_valid():
            form.save()
            messages.success(request, 'Aluno editado com sucesso!')
            return redirect('lista_alunos')

    else:
        form = AlunoForm(instance=aluno)

    return render(request, 'alunos/editar_aluno.html', {'form': form})


def excluir_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)

    if request.method == 'POST':
        aluno.delete()
        messages.success(request, 'Aluno excluído com sucesso!')
        return redirect('lista_alunos')

    return render(request, 'alunos/confirmar_exclusao.html', {'aluno': aluno})


def lista_materias(request):
    materias = Materia.objects.all()

    return render(request, 'alunos/lista_materias.html', {
        'materias': materias
    })


def gerenciar_materias(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)

    materias = Materia.objects.filter(curso=aluno.curso)

    if request.method == "POST":
        materias_ids = request.POST.getlist('materias')
        aluno.materias.set(materias_ids)

        messages.success(request, 'Matérias atualizadas com sucesso!')

        return redirect('gerenciar_materias', aluno_id=aluno.id)

    return render(request, 'alunos/gerenciar_materias.html', {
        'aluno': aluno,
        'materias': materias
    })