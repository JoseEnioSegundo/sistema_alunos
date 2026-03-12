# 📖 Guia de Uso - Sistema de Gerenciamento de Alunos

Um guia completo e prático para usar todas as funcionalidades do sistema.

---

## 🚀 Iniciando o Sistema

### 1. Ativar ambiente virtual
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 2. Iniciar servidor
```bash
python manage.py runserver
```

Acesse em: **http://localhost:8000**

### 3. Acessar painel administrativo
```
http://localhost:8000/admin
```
**Usuário:** admin  
**Senha:** (a senha que você criou com `python manage.py createsuperuser`)

---

## 💻 Funcionalidades Principais

### 📊 Dashboard (Página Inicial)

Ao entrar no sistema, você vê:

- **4 Cartões de Estatísticas**
  - Total de alunos cadastrados
  - Total de matérias
  - Total de cursos
  - Total de notas lançadas

- **Últimas Notas Lançadas** - Tabela com as 5 avaliações mais recentes
- **Melhores Desempenhos** - Ranking dos 5 alunos com melhor média

**Dica:** Clique em qualquer aluno para ver seu perfil completo!

---

### 👥 Gerenciar Alunos

#### **Listar Alunos**
- **URL:** `http://localhost:8000/alunos/`
- **O que você vê:**
  - Tabela com todos os alunos cadastrados
  - Filtro por curso
  - Busca por nome ou matrícula
  - Ações: Ver, Editar, Gerenciar Matérias, Ver Boletim, Desativar

#### **Cadastrar Novo Aluno**
- **URL:** `http://localhost:8000/alunos/cadastrar/`
- **Preencha:**
  - Nome completo
  - Email (deve ser único)
  - Curso
  - Data de nascimento
  - Telefone (opcional)
  - Endereço (opcional)
- **Clique:** "Salvar"
- **Resultado:** Aluno cadastrado com matrícula automática

#### **Editar Aluno**
- **Na lista de alunos**, clique no botão "✏️ Editar"
- **Ou acesse:** `http://localhost:8000/alunos/{id}/editar/`
- **Modifique** os dados desejados
- **Clique:** "Atualizar"

#### **Ver Perfil do Aluno**
- **Na lista de alunos**, clique no nome do aluno
- **Ou acesse:** `http://localhost:8000/alunos/{id}/perfil/`
- **Informações disponíveis:**
  - Dados pessoais completos
  - Matérias em que está matriculado
  - Últimas 5 notas lançadas
  - Desempenho por matéria

#### **Desativar Aluno**
- **Na lista de alunos**, clique no botão "🗑️ Desativar"
- **Importante:** Isso marca o aluno como inativo, mas mantém todos os dados!
- **Confirme** a exclusão
- **Resultado:** Aluno não aparece mais nas listas normais

---

### 📚 Gerenciar Matérias do Aluno

#### **Atualizar Matérias**
- **Na lista de alunos**, clique no botão "📚 Matérias"
- **Ou acesse:** `http://localhost:8000/alunos/{id}/materias/`
- **O que você vê:**
  - Listagem de todas as matérias do curso do aluno
  - Checkbox ao lado de cada matéria
  - Matérias já associadas aparecem marcadas ✓

#### **Adicionar Matéria**
- Marque o checkbox da matéria desejada
- Clique "Salvar Matérias"
- **Resultado:** Aluno agora está matriculado nessa matéria

#### **Remover Matéria**
- Desmarque o checkbox da matéria
- Clique "Salvar Matérias"
- **Resultado:** Aluno removido dessa matéria

---

### 📋 Notas e Boletim

#### **Listar Todas as Notas**
- **URL:** `http://localhost:8000/notas/`
- **Filtros disponíveis:**
  - Por aluno
  - Por matéria
  - Por tipo de avaliação
  - Por período (data inicial e final)
- **Cor das notas:**
  - 🟢 Verde: Nota ≥ 7.0 (Bom desempenho)
  - 🟡 Amarelo: 5.0 ≤ Nota < 7.0 (Recuperação)
  - 🔴 Vermelho: Nota < 5.0 (Abaixo do esperado)

#### **Lançar Nota**
- **URL:** `http://localhost:8000/notas/lancar/`
- **Preencha:**
  - **Aluno:** Selecione qual aluno (só aparecem alunos com matérias!)
  - **Matéria:** Selecione qual matéria (baseado nas matérias do aluno)
  - **Valor:** Digite de 0 a 10
  - **Data da Avaliação:** Quando foi a prova/trabalho
  - **Tipo de Avaliação:**
    - Prova (P)
    - Trabalho (T)
    - Atividade (A)
    - Exercício (E)
    - Projeto (Pr)
  - **Observação:** Comentários adicionais (opcional)
- **Clique:** "Salvar Nota"

**Atenção:** Um aluno só pode ter UMA nota por tipo de avaliação na mesma data para a mesma matéria!

#### **Editar Nota**
- **Na lista de notas**, clique no botão "✏️" da nota
- **Ou acesse:** `http://localhost:8000/notas/{id}/editar/`
- **Modifique** o valor ou observação
- **Clique:** "Atualizar"

#### **Deletar Nota**
- **Na lista de notas**, clique no botão "🗑️" da nota
- **Confirme** a exclusão
- **Resultado:** Nota removida do sistema

#### **Ver Boletim do Aluno**
- **Via lista de alunos:** Clique em um aluno → "📈 Boletim"
- **Ou acesse:** `http://localhost:8000/alunos/{id}/boletim/`
- **O que você vê:**
  - Todas as matérias do aluno
  - Notas de cada avaliação em cada matéria
  - **Média por matéria** calculada automaticamente
  - **Status:**
    - 🟢 **Aprovado:** Média ≥ 7.0
    - 🟡 **Recuperação:** 5.0 ≤ Média < 7.0
    - 🔴 **Reprovado:** Média < 5.0
  - **Média Geral** de todas as matérias

---

### 🎓 Gerenciar Cursos (Admin)

- **URL:** `http://localhost:8000/admin/alunos/curso/`
- **O que fazer:**
  - Visualizar todos os cursos
  - Ver total de alunos por curso
  - Editar informações do curso
  - Marcar como ativo/inativo
  - Adicionar descrição

---

### 📖 Gerenciar Matérias (Admin)

- **URL:** `http://localhost:8000/admin/alunos/materia/`
- **O que fazer:**
  - Visualizar todas as matérias
  - Filtrar por curso
  - Ver professor responsável
  - Ver carga horária
  - Editar informações

---

## 🔍 Filtros e Buscas

### Busca de Alunos
1. Vá para "Alunos" → "Lista de Alunos"
2. Use o campo de busca para procurar por:
   - Nome do aluno
   - Matrícula
3. Selecione um curso no dropdown para filtrar

### Filtro de Notas
1. Vá para "Notas" → "Listar Notas"
2. Use os filtros para encontrar notas específicas:
   - Selecione um aluno
   - Selecione uma matéria
   - Escolha tipo de avaliação
   - Defina período (de - até data)
3. Clique em "Filtrar"

---

## 🔐 Admin Panel

### Acessar
- **URL:** `http://localhost:8000/admin/`
- **Login com:** Superusuário que você criou

### O Que Fazer No Admin

#### Gerenciar Alunos
- Visualizar todos os alunos
- Filtrar por: Curso, Status (ativo/inativo), Data de nascimento
- Buscar por: Nome, Email, Matrícula
- Ver idade calculada automaticamente
- Editar dados diretamente

#### Gerenciar Cursos
- Listar todos os cursos
- Ver total de alunos matriculados
- Filtrar por status
- Editar nome e descrição

#### Gerenciar Matérias
- Listar todas as matérias
- Filtrar por curso e status
- Buscar por nome
- Ver professor e carga horária

#### Gerenciar Notas
- Listar todas as avaliações
- Timeline por data
- Buscar por aluno
- Filtrar por tipo de avaliação
- Ver observações
- Editar valores

---

## 💡 Dicas e Truques

### 🎯 Calcular Média Manualmente

Se quiser calcular a média de um aluno em uma matéria:

**Fórmula:**
```
Média = (Soma de todas as notas) / (Quantidade de notas)
```

**Exemplo:**
```
Notas em Português: 8.0, 7.5, 9.0
Média = (8.0 + 7.5 + 9.0) / 3 = 24.5 / 3 = 8.17
Status: Aprovado ✅
```

### 🚀 Dicas de Performance

1. **Use filtros** para encontrar dados rapidamente
2. **Paginação automática** - O sistema mostra 20 registros por página
3. **Busca avançada** - Combine múltiplos filtros para resultados precisos

### 📱 Responsivo

O sistema funciona em:
- ✅ Desktop
- ✅ Tablet
- ✅ Mobile (com scroll horizontal em tabelas)

### 🎨 Cores Significativas

- 🔵 **Azul** - Informações padrão
- 🟣 **Roxo** - Destaques e links
- 🟢 **Verde** - Sucesso, aprovado
- 🔴 **Vermelho** - Perigo, reprovado
- 🟡 **Amarelo** - Aviso, recuperação

---

## ❌ Troubleshooting

### "Não consigo cadastrar um aluno"
- Verifique se o email já existe no sistema
- Verifique se preencheu todos os campos obrigatórios
- Tente atualizar a página

### "Não consigo lançar nota"
- Certifique-se de que o aluno está matriculado em alguma matéria
- Verifique se a matéria selecionada é uma das matérias do aluno
- Note: Não pode ter duas notas do mesmo tipo na mesma data

### "Aluno não aparece na busca"
- Verifique se o aluno está marcado como ativo
- Tente filtrar por curso

### "Servidor não inicia"
```bash
# Rode as migrações
python manage.py migrate

# Verifique o banco de dados
python manage.py check

# Reinicie o servidor
python manage.py runserver
```

---

## 📞 Suporte Rápido

| Problema | Solução |
|----------|---------|
| Esquecer senha | Execute: `python manage.py changepassword admin` |
| Limpar dados | Delete `db.sqlite3` e execute: `python manage.py migrate && python manage.py createsuperuser` |
| Repor dados | Execute: `python populate_db.py && python populate_notas.py` |
| Verificar status | Execute: `python manage.py check` |

---

## 🎓 Fluxo Completo de Uso

### Passo 1: Criar Cursos
1. Admin panel → Cursos → Adicionar curso
2. Preencha nome e descrição

### Passo 2: Criar Matérias
1. Admin panel → Matérias → Adicionar matéria
2. Selecione o curso, professor, carga horária

### Passo 3: Cadastrar Alunos
1. Dashboard → Novo Aluno
2. Preencha dados pessoais
3. Selecione o curso

### Passo 4: Matricular em Matérias
1. Vá para lista de alunos
2. Clique "Gerenciar Matérias"
3. Selecione as matérias
4. Salve

### Passo 5: Lançar Notas
1. Vá para Notas → Lançar Nota
2. Selecione aluno e matéria
3. Preencha valor e tipo
4. Salve

### Passo 6: Consultar Boletim
1. Vá para lista de alunos
2. Clique no aluno → "Ver Boletim"
3. Consulte notas e status

---

## 🎉 Conclusão

Você domina o sistema! Para qualquer dúvida, consulte esté guia ou acesse o código comentado no repositório.

**Bom uso!** 🚀
