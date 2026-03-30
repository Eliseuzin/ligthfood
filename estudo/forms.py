#agora, iremos criar uma aplicaçao mais segura sobre o formulario e banco de dados
#1- instalar pip install flask_wtf
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,IntegerField, TextAreaField
# EqualTo verifica se um campo é == ao outro
# para a validaçao do email precisamos instalar pip install email_validator
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from estudo import db
from estudo.models import User,Store

from werkzeug.security import check_password_hash,generate_password_hash
# Escolha um único sistema de hash no seu projeto. 
# Se você está usando werkzeug.security.generate_password_hash()
#  para criar os hashes, use sempre check_password_hash() para verificar.
# Você usou generate_password_hash(..., method='scrypt') (do werkzeug) para salvar a senha.
# Mas tentou verificar com bcrypt.check_password_hash(...), o que causou:

#recuperaçao de senha
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from wtforms.validators import DataRequired, Email

#redefinir senha
# from flask_wtf import FlaskForm
# from wtforms import PasswordField, SubmitField
# from wtforms.validators import DataRequired, EqualTo


class UserForm(FlaskForm):
    nome= StringField('Nome', validators=[DataRequired()])
    sobrenome=StringField('Sobrenome', validators=[DataRequired()])
    endereco=StringField('Endereço', validators=[DataRequired()])
    complemento=StringField('Complemento(cs/app)', validators=[DataRequired()])
    celular=IntegerField('Celular', validators=[DataRequired()])
    email=StringField('Email', validators=[DataRequired()])
    senha=PasswordField('Senha', validators=[DataRequired()])
    confirmarsenha=PasswordField('Confirmar senha', validators=[DataRequired(message='Campo obrigatorio!'), EqualTo('senha', message='As senhas devem ser iguais!')])
    btnSubmit=SubmitField('Cadastrar usuário')
# flask_bcrypt faz a conversão internamente, então se você usar
#  .encode(), ele vai quebrar com erros como o ValueError: Invalid salt.
# self.senha.data já é uma string como "minhasenha123"
# Passar .encode('utf-8') transforma isso em b'minhasenha123'
# Flask-Bcrypt não aceita bytes nesse método, e isso pode
#  resultar em hashs inválidos (como o erro Invalid salt)
# Obter a senha do formulário	self.senha.data
# Gerar o hash corretamente	bcrypt.generate_password_hash(self.senha.data.encode('utf-8'))
# Salvar no banco	... .decode('utf-8') para virar str e ser compatível com o banco


    def save(self):
        senha_hash=generate_password_hash(self.senha.data)
        user=User(
            nome=self.nome.data,
            sobrenome=self.sobrenome.data,
            email=self.email.data,
            senha=senha_hash,
            endereco=self.endereco.data,
            complemento=self.complemento.data,
            celular=self.celular.data,

        )
        db.session.add(user)
        db.session.commit()
        return user
#  class Loginform(FlaskForm):


class StoreForm(FlaskForm):
    nome=StringField('Nome(pessoal):', validators=[DataRequired()])
    sobrenome=StringField('Sobrenome(pessoal):', validators=[DataRequired()])
    email=StringField('Email da loja:', validators=[DataRequired()])
    senha=PasswordField('Senha:', validators=[DataRequired()])
    celularp=IntegerField('Celular(pessoal):',validators=[DataRequired()])
    confirmarsenha=PasswordField('Confirmar senha:', validators=[DataRequired()])
    cnpj=IntegerField('CNPJ da loja:', validators=[DataRequired()])
    nomedaloja=StringField('Nome da loja:', validators=[DataRequired()])
    nextreferencia=StringField('Referência mais próxima da loja:', validators=[DataRequired()])
    endereco=StringField('Endereço da loja:', validators=[DataRequired()])
    btnSubmit=SubmitField('Cadastrar loja:')
    
    #saving database
    def save(self):
        senha_hash=generate_password_hash(self.senha.data)
        store=Store(
            nome=self.nome.data,
            sobrenome=self.sobrenome.data,
            email=self.email.data,
            senha=senha_hash,
            celularp=self.celularp.data,
            cnpj=self.cnpj.data,
            nomedaloja=self.nomedaloja.data,
            nextreferencia=self.nextreferencia.data,
            endereco=self.endereco.data
        )
        db.session.add(store)
        db.session.commit()
        return store
    

#há necessidade de criar duas class, caso contrário a segunda subescreve a primeira
#login clientes
class LoginForm(FlaskForm):
    email=StringField('E-mail', validators=[DataRequired(),Email()])
    senha=PasswordField('Senha', validators=[DataRequired()])
    btnSubmit=SubmitField('Entrar')
    #varificação com entrada no banco user

    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if not user:
            raise ValidationError('E-mail não encontrado, por favor, verifique o e-mail digitado!')
        # armazenar o usuario encontrado
        self.user=user
    
    def validate_senha(self,senha):
        # só valida se o email for valido e usuário existir
        user=getattr(self,'user',None)
        if user is None:
             #  evita validação dupla caso o email falhar
             return
        if not check_password_hash(user.senha,senha.data):
            raise ValidationError('Senha incorreta, por favor, verifique a senha digitada!')
        #login lojista
class LoginStore(FlaskForm):
    email=StringField('E-mail da loja', validators=[DataRequired(),Email()])
    senha=PasswordField('Senha', validators=[DataRequired()])
    btnSubmit=SubmitField('Entrar')
        #varificação com entrada no banco Store

    def validate_email(self,email):
        store=Store.query.filter_by(email=email.data).first()
        if not store:
            raise ValidationError('E-mail não encontrado, por favor, verifique o e-mail digitado!')
        #armazenar o usuário encontrado
        self.store=store

    def validate_senha(self,senha):
        #só valida se o email for valido e usuário existir
        store=getattr(self,'store', None)
        if store is None:
            #evita validação dupla caso email falhar
            return
        if not check_password_hash(store.senha,senha.data):
            raise ValidationError('Senha incorreta, por favor, verifique a senha digitada!')
        

class PedidoRecuperacaoForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Enviar link de recuperação')




class RedefinirSenhaForm(FlaskForm):
    senha = PasswordField('Nova senha', validators=[DataRequired()])
    confirmar_senha = PasswordField('Confirmar senha', validators=[
        DataRequired(),
        EqualTo('senha', message='As senhas devem ser iguais.')
    ])
    submit = SubmitField('Redefinir senha')

#atualizar cadastro usuário
class AtualizarUsuarioForm(FlaskForm):
    nome = StringField('Nome::', validators=[DataRequired()])
    sobrenome = StringField('Sobrenome:', validators=[DataRequired()])
    email = StringField('Email:', validators=[DataRequired(), Email()])
    endereco=StringField('Endereço:', validators=[DataRequired()])
    complemento=StringField('Complemento:', validators=[DataRequired()])
    celular=StringField('Celular:', validators=[DataRequired()])
    senha = PasswordField('Nova senha: (opcional)')
    confirmar_senha = PasswordField('Confirmar nova senha:', validators=[
        EqualTo('senha', message='As senhas devem ser iguais.')
    ])
    submit = SubmitField('Atualizar')

#atualizar cadastro lojista
class AtualizarLojistaForm(FlaskForm):
    nome=StringField('Nome pessoal:',validators=[DataRequired()])
    sobrenome=StringField('Sobrenome:', validators=[DataRequired()])
    email=StringField('Email:', validators=[DataRequired()])
    celularp=StringField('Celular pessoal:', validators=[DataRequired()])
    nomedaloja=StringField('Nome da loja', validators=[DataRequired()])
    nextreferencia=StringField('Referência próxima à loja:', validators=[DataRequired()])
    cnpj=StringField('Cnpj:', validators=[DataRequired()])
    endereco=StringField('Endereço da loja:', validators=[DataRequired()])
    senha= PasswordField('Nova senha (opcional):')
    confirmar_senha=PasswordField('Confimar nova senha:', validators=[EqualTo('senha',message='As senhas devem ser iguais')])
    submit=SubmitField('Atualizar')

# formulario de produtos para CRUD

# from flask_wtf import FlaskForm
# from wtforms import StringField, TextAreaField, SubmitField
from wtforms import DecimalField, BooleanField
# from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed

class ProdutoForm(FlaskForm):
    nome = StringField('Nome do produto:', validators=[DataRequired()])
    descricao = TextAreaField('Descrição:')
    preco = DecimalField('Preço:', validators=[DataRequired()])
    categoria = StringField('Categoria:')
    ativo = BooleanField('Ativo:')
    imagem = FileField('Imagem do produto:', validators=[
        FileAllowed(['jpg', 'jpeg', 'png', 'webp'], 'Ápenas imagens são permitidas!')])
    submit = SubmitField('Salvar')

# fim do formulário de produtos para CRUD
