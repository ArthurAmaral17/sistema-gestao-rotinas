[README.md](https://github.com/user-attachments/files/26694041/README.md)
# Sistema de Gestao de Rotinas

Aplicacao backend desenvolvida em Python com Flask para gerenciamento de rotinas pessoais. Permite que usuarios se cadastrem, criem rotinas e registrem execucoes diarias, com validacao de regras de negocio.

---

## Tecnologias utilizadas

- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Login
- Flask-WTF
- SQLite
- Bootstrap 5

---

## Estrutura do banco de dados

O sistema possui 4 tabelas:

### usuarios
Armazena os dados dos usuarios cadastrados.

| Campo      | Tipo         | Descricao              |
|------------|--------------|------------------------|
| id         | Integer (PK) | Identificador unico    |
| nome       | String(100)  | Nome do usuario        |
| email      | String(120)  | Email (unico)          |
| senha_hash | String(128)  | Senha criptografada    |

### categorias
Agrupa rotinas por tipo (ex: Saude, Estudos, Exercicio).

| Campo | Tipo         | Descricao           |
|-------|--------------|---------------------|
| id    | Integer (PK) | Identificador unico |
| nome  | String(64)   | Nome da categoria   |

### rotinas
Rotinas criadas pelos usuarios.

| Campo        | Tipo         | Descricao                          |
|--------------|--------------|------------------------------------|
| id           | Integer (PK) | Identificador unico                |
| titulo       | String(100)  | Titulo da rotina                   |
| descricao    | Text         | Descricao opcional                 |
| ativa        | Boolean      | Se a rotina esta ativa ou nao      |
| usuario_id   | Integer (FK) | Referencia ao usuario dono         |
| categoria_id | Integer (FK) | Referencia a categoria             |

### execucoes_diarias
Registros de execucao de cada rotina por dia.

| Campo      | Tipo         | Descricao                       |
|------------|--------------|---------------------------------|
| id         | Integer (PK) | Identificador unico             |
| data       | Date         | Data da execucao                |
| concluida  | Boolean      | Se foi concluida                |
| rotina_id  | Integer (FK) | Referencia a rotina executada   |
| usuario_id | Integer (FK) | Referencia ao usuario           |

### Relacionamentos
- `usuarios` 1:N `rotinas` (um usuario tem varias rotinas)
- `categorias` 1:N `rotinas` (uma categoria agrupa varias rotinas)
- `rotinas` 1:N `execucoes_diarias` (uma rotina tem varios registros de execucao)

---

## Rotas da aplicacao

### Autenticacao (`/auth`)
| Metodo | Rota             | Descricao              |
|--------|------------------|------------------------|
| GET    | /auth/login      | Pagina de login        |
| POST   | /auth/login      | Processa o login       |
| GET    | /auth/register   | Pagina de cadastro     |
| POST   | /auth/register   | Processa o cadastro    |
| GET    | /auth/logout     | Encerra a sessao       |

### Rotinas (`/rotinas`)
| Metodo | Rota                  | Descricao                   |
|--------|-----------------------|-----------------------------|
| GET    | /rotinas/             | Lista as rotinas do usuario |
| GET    | /rotinas/criar        | Formulario de nova rotina   |
| POST   | /rotinas/criar        | Cria uma nova rotina        |
| GET    | /rotinas/editar/<id>  | Formulario de edicao        |
| POST   | /rotinas/editar/<id>  | Atualiza a rotina           |
| GET    | /rotinas/excluir/<id> | Remove a rotina             |
| GET    | /rotinas/executar/<id>| Registra execucao do dia    |

### Categorias (`/categorias`)
| Metodo | Rota                     | Descricao              |
|--------|--------------------------|------------------------|
| GET    | /categorias/             | Lista as categorias    |
| GET    | /categorias/criar        | Formulario de criacao  |
| POST   | /categorias/criar        | Cria uma categoria     |
| GET    | /categorias/excluir/<id> | Remove uma categoria   |

---

## Regras de negocio

### 1. Execucao unica por dia
Uma rotina so pode ser registrada como executada uma unica vez por dia. Se o usuario tentar executar novamente no mesmo dia, o sistema bloqueia e exibe uma mensagem de aviso.

### 2. Rotina deve estar ativa
Somente rotinas com status `ativa = True` podem ter execucoes registradas. Rotinas inativas ficam com o botao "Executar" desabilitado na interface.

### 3. Cada usuario ve apenas suas proprias rotinas
O sistema filtra as rotinas pelo `usuario_id` da sessao ativa, garantindo isolamento entre usuarios.

### 4. Validacao de email duplicado
Nao e permitido cadastrar dois usuarios com o mesmo email. O sistema verifica antes de inserir e exibe mensagem de erro.

---

## Instrucoes para execucao

### 1. Clonar o repositorio
```bash
git clone <url-do-repositorio>
cd sistema_rotinas
```

### 2. Criar e ativar o ambiente virtual
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Instalar as dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar as variaveis de ambiente
Crie um arquivo `.env` na raiz do projeto com o seguinte conteudo:
```
SECRET_KEY=chave-super-secreta-2026
```

### 5. Criar o banco de dados via migrations
```bash
flask db upgrade
```

### 6. Rodar a aplicacao
```bash
python run.py
```

Acesse em: http://127.0.0.1:5000

---

## Estrutura de pastas

```
sistema_rotinas/
├── app/
│   ├── auth/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── categorias/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── rotinas/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── main/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── categorias/
│   │   └── rotinas/
│   ├── __init__.py
│   ├── forms.py
│   └── models.py
├── migrations/
├── instance/
├── venv/
├── .env
├── .gitignore
├── config.py
├── requirements.txt
└── run.py
```
