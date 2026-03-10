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
