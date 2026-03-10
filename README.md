
# Sistema de Gerenciamento de Alunos | Student Management System

---

## 📋 Table of Contents | Índice

- [English](#-english) 🇺🇸
- [Português](#-português) 🇧🇷

---

## 🇺🇸 English

### Overview

**Sistema de Gerenciamento de Alunos** is a comprehensive web-based student management system built with Django. This application provides a complete solution for managing students, courses, and subjects, including features for student enrollment, subject assignment, and administrative operations.

### ✨ Features

- **Student Management**: Register, edit, view, and delete student records
- **Enrollment Management**: Assign and manage subjects for each student
- **Search Functionality**: Advanced search with filters by name, course, and enrollment number
- **Pagination**: Efficient list navigation with page-based browsing
- **Subject Management**: Manage subjects with professor assignments
- **Course Management**: Organize students by courses
- **Admin Dashboard**: Django admin panel for complete system administration
- **Responsive Design**: Clean and professional user interface

### 🛠️ Technology Stack

- **Backend**: Django 6.0.2
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3
- **Python Version**: 3.x

### 📋 Requirements

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package manager)
- Virtual Environment (venv or virtualenv)

### 🚀 Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/JoseEnioSegundo/sistema_alunos.git
cd sistema_alunos
```

#### 2. Create and Activate Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies

```bash
pip install django==6.0.2
```

#### 4. Apply Migrations

```bash
python manage.py migrate
```

#### 5. Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

#### 6. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

### 📱 Usage

#### Accessing the Application

1. **Main Interface**: Navigate to `http://127.0.0.1:8000/alunos/` to access the student list
2. **Admin Panel**: Go to `http://127.0.0.1:8000/admin/` and log in with your superuser credentials

#### Main Features

- **View Students**: Browse all registered students with pagination
- **Add Student**: Click "Cadastrar Aluno" to register a new student
- **Edit Student**: Click the edit icon to modify student information
- **Delete Student**: Remove students from the system with confirmation
- **Search**: Use the search bar to find students by name, course, or enrollment number
- **Manage Subjects**: Assign and manage subjects for each student

### 📁 Project Structure

```
sistema_alunos/
├── alunos/                          # Main application
│   ├── migrations/                  # Database migrations
│   ├── templates/alunos/
│   │   ├── cadastrar_aluno.html    # Student registration form
│   │   ├── confirmar_exclusao.html # Delete confirmation
│   │   ├── editar_aluno.html       # Student edit form
│   │   ├── gerenciar_materias.html # Manage subjects
│   │   ├── lista_alunos.html       # Student list view
│   │   └── lista_materias.html     # Subject list view
│   ├── admin.py                     # Admin configuration
│   ├── apps.py                      # App configuration
│   ├── forms.py                     # Form definitions
│   ├── models.py                    # Database models
│   ├── urls.py                      # URL routing
│   ├── views.py                     # View logic
│   └── tests.py                     # Unit tests
├── config/                          # Project configuration
│   ├── settings.py                  # Django settings
│   ├── urls.py                      # Main URL configuration
│   ├── asgi.py                      # ASGI configuration
│   └── wsgi.py                      # WSGI configuration
├── static/
│   └── css/
│       └── style.css                # Application styles
├── templates/
│   └── base.html                    # Base template
├── manage.py                        # Django management script
└── db.sqlite3                       # SQLite database
```

### 📊 Database Models

#### Aluno (Student)
- `nome`: Student's full name
- `email`: Student's email address
- `matricula`: Unique enrollment number
- `curso`: Foreign key to Course
- `data_nascimento`: Date of birth
- `materias`: Many-to-many relationship with Subjects

#### Materia (Subject)
- `nome`: Subject name
- `professor`: Professor's name
- `curso`: Foreign key to Course

#### Curso (Course)
- `nome`: Course name

### 🔧 Configuration

#### Key Settings (config/settings.py)

- **DEBUG**: Currently set to `True` (change to `False` in production)
- **ALLOWED_HOSTS**: Add your domain or IP addresses for production
- **DATABASES**: SQLite3 database configuration
- **INSTALLED_APPS**: Django apps including the main 'alunos' app

### 🚨 Important Notes for Production

⚠️ **Before deploying to production:**

1. Set `DEBUG = False` in settings.py
2. Change `SECRET_KEY` to a secure, random value
3. Configure `ALLOWED_HOSTS` with your domain
4. Set up a production database (PostgreSQL recommended)
5. Configure static files serving
6. Use a production-grade web server (Gunicorn, uWSGI)
7. Implement HTTPS
8. Set up proper backup procedures

### 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### 📄 License

This project is open source and available under the MIT License.

### 📞 Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

## 🇧🇷 Português

### Visão Geral

**Sistema de Gerenciamento de Alunos** é um sistema web completo para gerenciamento de estudantes construído com Django. Esta aplicação oferece uma solução completa para gerenciar alunos, cursos e disciplinas, incluindo recursos para inscrição de alunos, atribuição de disciplinas e operações administrativas.

### ✨ Funcionalidades

- **Gerenciamento de Alunos**: Registrar, editar, visualizar e deletar registros de alunos
- **Gerenciamento de Inscrições**: Atribuir e gerenciar disciplinas para cada aluno
- **Busca Avançada**: Pesquisa com filtros por nome, curso e número de matrícula
- **Paginação**: Navegação eficiente em listas com navegação baseada em páginas
- **Gerenciamento de Disciplinas**: Gerenciar disciplinas com atribuição de professores
- **Gerenciamento de Cursos**: Organizar alunos por cursos
- **Painel de Administração**: Painel de administração Django para administração completa do sistema
- **Design Responsivo**: Interface de usuário limpa e profissional

### 🛠️ Stack de Tecnologias

- **Backend**: Django 6.0.2
- **Banco de Dados**: SQLite3
- **Frontend**: HTML5, CSS3
- **Versão Python**: 3.x

### 📋 Requisitos

Antes de começar, certifique-se de ter o seguinte instalado:

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Ambiente Virtual (venv ou virtualenv)

### 🚀 Instalação

#### 1. Clone o Repositório

```bash
git clone https://github.com/JoseEnioSegundo/sistema_alunos.git
cd sistema_alunos
```

#### 2. Crie e Ative o Ambiente Virtual

**No Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**No macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Instale as Dependências

```bash
pip install django==6.0.2
```

#### 4. Aplique as Migrações

```bash
python manage.py migrate
```

#### 5. Crie um Superusuário (Conta de Administrador)

```bash
python manage.py createsuperuser
```

Siga os prompts para criar sua conta de administrador.

#### 6. Execute o Servidor de Desenvolvimento

```bash
python manage.py runserver
```

A aplicação estará disponível em `http://127.0.0.1:8000/`

### 📱 Uso

#### Acessando a Aplicação

1. **Interface Principal**: Acesse `http://127.0.0.1:8000/alunos/` para acessar a lista de alunos
2. **Painel de Administração**: Vá para `http://127.0.0.1:8000/admin/` e faça login com suas credenciais de superusuário

#### Funcionalidades Principais

- **Visualizar Alunos**: Navegue todos os alunos registrados com paginação
- **Adicionar Aluno**: Clique em "Cadastrar Aluno" para registrar um novo aluno
- **Editar Aluno**: Clique no ícone de editar para modificar informações do aluno
- **Deletar Aluno**: Remova alunos do sistema com confirmação
- **Pesquisar**: Use a barra de pesquisa para encontrar alunos por nome, curso ou número de matrícula
- **Gerenciar Disciplinas**: Atribua e gerencie disciplinas para cada aluno

### 📁 Estrutura do Projeto

```
sistema_alunos/
├── alunos/                          # Aplicação principal
│   ├── migrations/                  # Migrações de banco de dados
│   ├── templates/alunos/
│   │   ├── cadastrar_aluno.html    # Formulário de registro de aluno
│   │   ├── confirmar_exclusao.html # Confirmação de exclusão
│   │   ├── editar_aluno.html       # Formulário de edição de aluno
│   │   ├── gerenciar_materias.html # Gerenciar disciplinas
│   │   ├── lista_alunos.html       # Visualização de lista de alunos
│   │   └── lista_materias.html     # Visualização de lista de disciplinas
│   ├── admin.py                     # Configuração de administrador
│   ├── apps.py                      # Configuração de aplicativo
│   ├── forms.py                     # Definições de formulários
│   ├── models.py                    # Modelos de banco de dados
│   ├── urls.py                      # Roteamento de URL
│   ├── views.py                     # Lógica de visualização
│   └── tests.py                     # Testes unitários
├── config/                          # Configuração do projeto
│   ├── settings.py                  # Configurações Django
│   ├── urls.py                      # Configuração principal de URL
│   ├── asgi.py                      # Configuração ASGI
│   └── wsgi.py                      # Configuração WSGI
├── static/
│   └── css/
│       └── style.css                # Estilos da aplicação
├── templates/
│   └── base.html                    # Template base
├── manage.py                        # Script de gerenciamento Django
└── db.sqlite3                       # Banco de dados SQLite
```

### 📊 Modelos de Banco de Dados

#### Aluno
- `nome`: Nome completo do aluno
- `email`: Email do aluno
- `matricula`: Número de matrícula único
- `curso`: Chave estrangeira para Curso
- `data_nascimento`: Data de nascimento
- `materias`: Relacionamento muitos-para-muitos com Disciplinas

#### Materia
- `nome`: Nome da disciplina
- `professor`: Nome do professor
- `curso`: Chave estrangeira para Curso

#### Curso
- `nome`: Nome do curso

### 🔧 Configuração

#### Configurações Principais (config/settings.py)

- **DEBUG**: Atualmente definido como `True` (mude para `False` em produção)
- **ALLOWED_HOSTS**: Adicione seu domínio ou endereços IP para produção
- **DATABASES**: Configuração de banco de dados SQLite3
- **INSTALLED_APPS**: Aplicativos Django incluindo o aplicativo main 'alunos'

### 🚨 Notas Importantes para Produção

⚠️ **Antes de fazer deploy em produção:**

1. Defina `DEBUG = False` em settings.py
2. Mude `SECRET_KEY` para um valor seguro e aleatório
3. Configure `ALLOWED_HOSTS` com seu domínio
4. Configure um banco de dados de produção (PostgreSQL recomendado)
5. Configure o servimento de arquivos estáticos
6. Use um servidor web para produção (Gunicorn, uWSGI)
7. Implemente HTTPS
8. Configure procedimentos adequados de backup

### 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se livre para enviar um Pull Request.

### 📄 Licença

Este projeto é de código aberto e está disponível sob a Licença MIT.

### 📞 Suporte

Para problemas, dúvidas ou sugestões, abra uma issue no GitHub.

---

**Author | Autor**: José Enio Segundo  
**Last Updated | Última Atualização**: Março 2026
=======
📚 Sistema de Gerenciamento de Alunos e Matérias

Este projeto foi desenvolvido com o objetivo de praticar conceitos de desenvolvimento web utilizando Python e Django, criando um sistema simples de gerenciamento acadêmico.

O sistema permite cadastrar alunos, cursos e matérias, além de possibilitar a associação de matérias aos alunos.

🚀 Funcionalidades

O sistema possui as seguintes funcionalidades:

Cadastro de alunos

Edição e exclusão de alunos

Listagem de alunos com paginação

Busca de alunos pelo nome

Cadastro de cursos

Cadastro de matérias

Associação de matérias a um aluno

Interface simples utilizando Bootstrap

🧠 Objetivo do Projeto

O objetivo principal deste projeto foi colocar em prática conceitos importantes de desenvolvimento web, como:

Arquitetura MVC (Model, View, Template) do Django

Relacionamentos entre modelos no banco de dados

Criação de formulários

Uso de views para lógica de aplicação

Organização de templates

Implementação de funcionalidades como busca e paginação

Além disso, o projeto serve como experiência prática para portfólio, demonstrando conhecimentos iniciais em desenvolvimento backend com Django.

🛠️ Tecnologias Utilizadas

Python

Django

HTML

Bootstrap

SQLite (banco de dados padrão do Django)

📂 Estrutura Básica do Projeto
projeto/
│
├── alunos/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── templates/
│   ├── base.html
│   ├── lista_alunos.html
│   ├── gerenciar_materias.html
│
├── db.sqlite3
└── manage.py
▶️ Como Executar o Projeto

Clone o repositório

git clone https://github.com/seu-usuario/seu-repositorio.git

Entre na pasta do projeto

cd seu-repositorio

Crie o ambiente virtual

python -m venv venv

Ative o ambiente virtual

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate

Instale as dependências

pip install django

Execute as migrações do banco de dados

python manage.py migrate

Inicie o servidor

python manage.py runserver

Acesse no navegador

http://127.0.0.1:8000
👨‍💻 Autor

Projeto desenvolvido por José Enio Ardino Segundo, estudante de Sistemas de Informação, com foco em aprendizado e prática de desenvolvimento web com Django.
>>>>>>> cf2bae23ed33589998f2208804247e6a59fc8b23
