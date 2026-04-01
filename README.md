# fulldatehamburgueira

# 🍔 Sistema Web de Gestão para Hamburgueria

Sistema web completo desenvolvido com Python e Flask para gerenciamento de produtos, pedidos e usuários (cliente e lojista).

---

## 🚀 Funcionalidades

### 👤 Cliente
- Criar conta
- Login e logout
- Visualizar produtos
- Adicionar ao carrinho
- Finalizar pedidos
- Histórico de pedidos

### 🏪 Lojista
- Login exclusivo
- Dashboard administrativo(futuro)
- Criar, editar e desativar produtos
- Upload de imagens
- Gerenciar pedidos

---

## 🛠 Tecnologias Utilizadas

- Python 3.12
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-Migrate
- Flask-WTF
- Flask-Bcrypt
- SQLite
- HTML, CSS e JavaScript

---

## 🔐 Segurança Implementada

- Hash de senha com Bcrypt
- Proteção contra SQL Injection via ORM
- Controle de acesso por tipo de usuário
- Proteção CSRF com Flask-WTF
- Upload seguro de arquivos

---

## 📂 Estrutura do Projeto

estudo>

static/
templates/

├── init.py
├── forms.py
├── models.py
├── routes.py
├── utils.py
├── verificar_senha_digitada.py

instance/
migrations/

creat.key.py
main.py
wsgi.py



---------------------------------------------------------


## 👨‍💻 Autor

Eliseu Matos da Silva

Projeto desenvolvido para estudo e prática de desenvolvimento backend com Flask.



## ▶ Como Executar o Projeto

```bash
git clone https://github.com/Eliseuzin/fulldatehamburgueira
cd fulldatehamburgueira

python -m venv venv
venv\Scripts\activate  # Windows

pip install -r requirements.txt

python main.py


