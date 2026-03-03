from django.shortcuts import render
from .models import Aluno
from django.shortcuts import redirect
from .forms import AlunoForm
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno
from .forms import AlunoForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

def lista_alunos(request):
    buscar = request.GET.get('buscar')

    if buscar:
        alunos_lista = Aluno.objects.filter(
            Q(nome__icontains=buscar) |
            Q(curso__icontains=buscar)|
            Q(matricula__icontains=buscar)
        )
    else:
        alunos_lista = Aluno.objects.all()

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



def excluir_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)

    if request.method == 'POST':
        aluno.delete()
        messages.success(request, 'Aluno excluído com sucesso!')
        return redirect('lista_alunos')

    return render(request, 'alunos/confirmar_exclusao.html', {'aluno': aluno})



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