from estudo import db

from datetime import datetime
from flask_login import UserMixin

#inicio do controle de login usuario
# significa que você está usando o Flask-Login, mas não definiu a função obrigatória user_loader — que é necessária para o login funcionar corretamente.

# ⚠️ Regra profissional simples (guarde isso)

# Se o sistema quebra sem o valor → nullable=False
# Se o sistema continua funcionando → nullable=True


class User(db.Model,UserMixin):
    #nullable=True, que dizer que o campo pode ficar vazio
    id=db.Column(db.Integer,primary_key=True)
    nome=db.Column(db.String(100), nullable=False)
    cep=db.Column(db.String(9), nullable=False)
    rua=db.Column(db.String(100), nullable=False)
    bairro=db.Column(db.String(50),nullable=False)
    cidade=db.Column(db.String(50), nullable=False)
    estado=db.Column(db.String(2), nullable=False)
    complemento=db.Column(db.String, nullable=False)
    celular=db.Column(db.String(20), nullable=False)
    sobrenome=db.Column(db.String(50), nullable=False)
    email=db.Column(db.String(100), nullable=False)
    senha=db.Column(db.String(50), nullable=False)

# evita da erro ao logo, pois o flask busca o id e sempre ira no pri meiro que encontar
    def get_id(self):
        return f"user:{self.id}"
    
 #fim do controle de login usuario

 #inicio do controle de login loja
class Store(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    nome=db.Column(db.String, nullable=False)
    sobrenome=db.Column(db.String, nullable=True)
    email=db.Column(db.String, nullable=False)
    celularp=db.Column(db.String(20), nullable=False)
    senha=db.Column(db.String, nullable=False)
    cnpj=db.Column(db.String(18), nullable=False)
    nomedaloja=db.Column(db.String, nullable=False)
    nextreferencia=db.Column(db.String, nullable=True)
    cep=db.Column(db.String(9), nullable=False)
    rua=db.Column(db.String(100), nullable=False)
    bairro=db.Column(db.String(50),nullable=False)
    cidade=db.Column(db.String(50), nullable=False)
    estado=db.Column(db.String(2), nullable=False)
    
# evita da erro ao logo, pois o flask busca o id e sempre ira no pri meiro que encontar
    def get_id(self):
        return f"store:{self.id}"
 #fim do controle de login loja

#inicio de salvar itens do carrinho
class Carrinho(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    itens = db.relationship('ItemCarrinho', backref='carrinho', lazy=True)

class ItemCarrinho(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    carrinho_id = db.Column(db.Integer, db.ForeignKey('carrinho.id'))
    nome_produto = db.Column(db.String(100))
    preco = db.Column(db.Float)
    quantidade = db.Column(db.Integer)

#fim de salvar itens do carrinho

# criando gerenciamento do pedidos

# from estudo import db


# model para produtos crud

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=True)
    descricao = db.Column(db.Text, nullable=True)
    preco = db.Column(db.Float, nullable=True)
    categoria = db.Column(db.String(80), nullable=True)
    ativo = db.Column(db.Boolean, default=True)
    imagem = db.Column(db.String(200), nullable=True)


    # 👇 ESTE CAMPO É OBRIGATÓRIO PARA LIGAR PRODUTO À LOJA (usuário)
    loja_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # opcional: relacionamento
    loja = db.relationship('User', backref='produtos')

# fim do model para produtos crud



#inicio do model para gerenciar os pedidos(status) de pagamentos
# from datetime import datetime

# class Pedidos(db.Model):
#     id = db.Column(db.Integer, primary_key=True)

#     loja_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#     cliente_nome = db.Column(db.String(120), nullable=False)
#     total = db.Column(db.Numeric(10,2), nullable=False)

#     status = db.Column(db.String(20), default='pendente')
#     criado_em = db.Column(db.DateTime, default=datetime.utcnow)


#fim do model para gerenciar os pedidos(status) de pagamentos





from flask_sqlalchemy import SQLAlchemy


class Pedidos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # inicio cliente
    cliente_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    cliente_nome = db.Column(db.String(100))
    celular = db.Column(db.String(20))
    # fim cliente
    
    # inicio loja
    loja_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # fim loja

    # inicio pedidos
    itens = db.Column(db.Text) #aqui colocaremos os dados do pedido
    subtotal = db.Column(db.Float)
    taxa_entrega = db.Column(db.Float)
    total = db.Column(db.Float)
    # fim pedidos

    # inicio entrega
    distancia = db.Column(db.Integer) #em metros
    tempo_entre_distancia = db.Column(db.String(30), default="Recebido")
    # fim entrega

    # inicio status do pedido
    status = db.Column(db.String(50))
    # fim status do pedido

    # inicio data do recebimento do pedido
    data_recebido = db.Column(db.DateTime, default=datetime.utcnow)
    # fim data do recebimento do pedido






#comando para criar o banco de dados
#flask db init
#é necessário apenas um banco de dados por projeto.
# para fazer roda as alteraçoes no banco de dados
# flask db migrate -m "mensagem"
# flask db upgrade

#apagar banco del database.db