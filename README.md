# 🖼️ Post Memes

Projeto divertido, onde qualquer pessoa pode postar memes e comentar sem precisar criar conta.

## 🚀 Funcionalidades

* Postar memes com apenas um nome (sem cadastro)
* Visualizar todos os memes postados
* Comentar em memes específicos sem login
* Interface simples e direta para interação rápida

## 🛠 Tecnologias Utilizadas

* Python
* Flask
* Flask-SQLAlchemy
* Flask-Migrate
* Jinja2
* PostgreSQL
* SQLAlchemy
* Alembic
* HTML5 + CSS3

## 📁 Estrutura de Pastas

```bash
.
├── app/
│   ├── controllers/
│   │   └── comentario_controller.py
│   │   └── meme_controller.py
│   ├── models/
│   │   └── __init__.py
│   │   └── comentario_model.py
│   │   └── meme_model.py
│   │   └── user_model.py
│   ├── services/
│   │   └── comentario_service.py
│   │   └── data_service.py
│   │   └── meme_service.py
│   ├── static/
│   │   └── uploads/
│   │   └── index.css
│   │   └── meme_detalhes.css
│   ├── templates/
│   │   └── index.html
│   │   └── meme_detalhes.html
│   ├── __init__.py
│   └── config.py
├── .gitignore
├── main.py
└── requirements.txt
```

## 💻 Como Rodar Localmente

```bash
# Clone o repositório
git clone https://github.com/Ivysonin/post_memes.git

# Acesse a pasta do projeto
cd post_memes

# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente virtual (Windows)
venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente
SECRET_KEY='chave-secreta-aqui'
DATABASE_URL='postgresql://usuário:senha@host:porta/nome_do_banco'

# Rode a aplicação
python main.py

# Acesse no navegador
http://localhost:5000
```

## 📖 Aprendizados

Durante o desenvolvimento do Post Memes, os principais focos foram:

* Criar uma aplicação web funcional com Flask e banco de dados
* Permitir interação sem autenticação, focando na simplicidade

## 🖼️ Imagem

<img width="1082" height="507" alt="Captura de tela de 2025-09-06 19-55-29" src="https://github.com/user-attachments/assets/29cbbae8-c2b9-40b0-87d5-6089bdde3434" />

## 📄 Licença

Este projeto está licenciado sob os termos da [Licença MIT](./LICENSE), com cláusula adicional de atribuição.
