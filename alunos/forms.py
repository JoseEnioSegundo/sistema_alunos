from django import forms
from .models import Aluno, Curso, Materia, Nota


# ========== Form para Cadastro e Edição de Alunos ==========
class AlunoForm(forms.ModelForm):
    """
    Formulário para criação e edição de alunos.
    Inclui validações e widgets personalizados do Bootstrap.
    """
    class Meta:
        model = Aluno
        fields = ['nome', 'email', 'matricula', 'curso', 'data_nascimento', 'telefone', 'endereco']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome completo'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email@exemplo.com'
            }),
            'matricula': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '2024000001',
                'readonly': True  # Matrícula não deve ser alterada após criação
            }),
            'curso': forms.Select(attrs={
                'class': 'form-control'
            }),
            'data_nascimento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(11) 99000-0000'
            }),
            'endereco': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Rua, número, complemento, cidade'
            }),
        }


# ========== Form para Gerenciamento de Matérias de Alunos ==========
class MateriasForm(forms.Form):
    """
    Formulário para seleção de matérias.
    Permite associar/desassociar matérias aos alunos.
    """
    def __init__(self, *args, materias=None, **kwargs):
        super().__init__(*args, **kwargs)
        
        if materias:
            # Cria um checkbox para cada matéria
            self.fields['materias'] = forms.ModelMultipleChoiceField(
                queryset=materias,
                widget=forms.CheckboxSelectMultiple(),
                required=False,
                label='Selecione as matérias'
            )


# ========== Form para Lançamento de Notas ==========
class NotaForm(forms.ModelForm):
    """
    Formulário para lançamento de notas dos alunos.
    Inclui validações de intervalo (0-10) e seleção de tipo de avaliação.
    """
    class Meta:
        model = Nota
        fields = ['aluno', 'materia', 'valor', 'tipo_avaliacao', 'observacao']
        widgets = {
            'aluno': forms.Select(attrs={
                'class': 'form-control',
                'id': 'id_aluno'
            }),
            'materia': forms.Select(attrs={
                'class': 'form-control',
                'id': 'id_materia'
            }),
            'valor': forms.NumberInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'step': '0.01',
                'min': '0',
                'max': '10',
                'placeholder': '0.00'
            }),
            'tipo_avaliacao': forms.Select(attrs={
                'class': 'form-control'
            }),
            'observacao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Observações sobre a avaliação (opcional)'
            }),
        }

    def clean_valor(self):
        """Valida se o valor da nota está entre 0 e 10"""
        valor = self.cleaned_data.get('valor')
        if valor is not None:
            if valor < 0 or valor > 10:
                raise forms.ValidationError('A nota deve estar entre 0 e 10.')
        return valor


# ========== Form para Busca de Notas ==========
class BuscaNotasForm(forms.Form):
    """
    Formulário para filtrar e buscar notas.
    Permite filtrar por aluno, matéria, tipo de avaliação e período.
    """
    aluno = forms.ModelChoiceField(
        queryset=Aluno.objects.all(),
        required=False,
        empty_label='Todos os alunos',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    materia = forms.ModelChoiceField(
        queryset=Materia.objects.all(),
        required=False,
        empty_label='Todas as matérias',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    data_inicio = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )
    
    data_fim = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )


# ========== Form para Filtro de Curso ==========
class FilterCursoForm(forms.Form):
    """
    Formulário simples para filtrar alunos por curso.
    """
    curso = forms.ModelChoiceField(
        queryset=Curso.objects.filter(ativo=True),
        required=False,
        empty_label='Todos os cursos',
        widget=forms.Select(attrs={'class': 'form-control'})
    )