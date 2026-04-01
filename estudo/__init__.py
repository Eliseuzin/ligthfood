from flask import Flask
#vamos começa a configura o nosso banco de dados
#pip install Flask-SQLAlchemy Flask-Migrate
#depois temos de import antes de app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# vamos deixa nosso nossas chaves mais seguras utilizando variaveis de ambiente
# pip install python-dotenv
from dotenv import load_dotenv
# inicio da nosso controle de login.
# pip install flask-login flask-bcrypt
# from flask_login import LoginManager
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
#verificaçao de email
from flask_mail import Mail
from flask import session
from flask_login import current_user

# responsavel por busca os valores
import os
load_dotenv('.env')

# ✅ Causa prováveis de erros:
# O problema não é no seu projeto, nem no código, mas sim porque o Python que está rodando o script não é o mesmo Python que tem o Flask-Login instalado.

# Apesar de o terminal mostrar (venv) ativado, o VS Code ou o terminal pode estar rodando o Python global (fora do venv).
# where python
# Se estiver certo, o primeiro caminho listado deve ser algo como:
# E:\bettersites\finishedhamburgeria\fulldatehamburgueira\venv\Scripts\python.exe

# Se estiver listando algo como:
# C:\Users\vin1z\AppData\...
# então você está rodando o Python errado, e o flask_login não está instalado lá.

# 💡 É o equivalente a dizer:
# "Ei, instale esse pacote exatamente neste projeto aqui, não importa o resto do sistema!"

# .\venv\Scripts\pip.exe install flask-bcrypt

#instartar nosso aplicativo
# app=Flask(__name__)

app = Flask(
    __name__,
    static_folder='static',
    static_url_path='/static'
)

# print("STATIC FOLDER:", app.static_folder)
# print("STATIC URL PATH:", app.static_url_path)


# Configurações do app (antes de criar mail, db, etc)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui'

# Agora inicialize as extensões
mail = Mail(app)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
# login_manager = LoginManager(app)
# bcrypt = Bcrypt(app)

#configurar o banco de dados
#quando criamos o banco de dados, ele chamará database.db
# app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('DATABASE_URI')
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(BASE_DIR, '..', 'database.db')  # raiz do projeto

app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.abspath(db_path)}"
#aumenta a prioridade, e evita o checking
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

print("DB REAL PATH:", os.path.abspath(db_path))
#mais para frente aprenderemos a deixa o nosso banco de dados mais seguro, sem deixa chaves de acesso livres
# app.config['SECRET_KEY']=os.getenv('SECRET_KEY')
app.config['SECRET_KEY']='8a97b281fcaf00eaee650eb9078eded3d3c0656406f7d8b103191d1fb7f3ef18598a55ae52791310f2e96b716d17c78de9e1'
db=SQLAlchemy(app)
migrate=Migrate(app, db)
#comando para criar o banco de dados
#flask db init
#é necessário apenas um banco de dados por projeto.

# pip install Flask-Mail

#inicio de controle de add imgagens ao produto
#import os(tive que fazer isto, pois estava criando outra página, consequentemene não abrindo img)
#INÍCIO
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#FIM

app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024  # 2 MB
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.jpeg', '.webp']

#fim de controle de add imgagens ao produto



#inicio do controle de login
from estudo.models import User, Store

login_manager=LoginManager(app)
# bcrypt=Bcrypt(app)
# controle de login
login_manager.login_view='login'



# fazendo teste com o login de cliente e loja
# significa que você está usando o Flask-Login, mas não definiu a função obrigatória user_loader — que é necessária para o login funcionar corretamente.
# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(user_id)

# está acontecendo porque você está tentando importar login_manager
# de dentro do models.py, mas o login_manager só é criado no
# __init__.py — e isso causa um "ciclo de importação" (circular import).

@login_manager.user_loader
def load_user(user_key):
    if not user_key:
        return None

    # formato novo: "tipo:id"
    if ":" in user_key:
        tipo, user_id = user_key.split(":")

        if tipo == "user":
            return User.query.get(int(user_id))
        elif tipo == "store":
            return Store.query.get(int(user_id))

    # 🔥 fallback (caso seja só número antigo)
    return User.query.get(int(user_key))



# evitar da erros de O Jinja não aceita funções Python como hasattr.
@app.context_processor
def inject_user_type():
    tipo = None

    if current_user.is_authenticated:
        # Verifica se o ID guardado começa com 'store:' ou 'user:'
        user_cookie = session.get('_user_id', '')
        if ':' in user_cookie:
            tipo = user_cookie.split(':')[0]

    return dict(tipo_usuario=tipo)



# importa as rotas
from estudo import routes 


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(BASE_DIR, 'database.db')

from estudo import models  # 🔥 importa tudo




# with app.app_context():
#     print("Criando tabelas agora...")
#     db.create_all()

# inspector = inspect(db.engine)
# print("Tabelas criadas:", inspector.get_table_names())

# with app.app_context():
#     db.create_all()