#pip install flask
from estudo import app,db
from flask import render_template, url_for 
from flask import redirect,flash
from flask_login import login_user, logout_user, current_user, login_required
from estudo.forms import LoginForm, LoginStore
from flask import session, request, jsonify
from estudo.models import ItemCarrinho, Carrinho

#AGORA, IREMOS CRIAR OS PASSOS DE Pedir link de recuperação
 # função que você deve implementar
# from flask import render_template, request, flash, redirect, url_for
from estudo.forms import PedidoRecuperacaoForm
from estudo.utils import gerar_token,enviar_email
from estudo.models import User, Store  # seu modelo de usuário

# E Página para redefinir senha
from estudo.forms import RedefinirSenhaForm
from estudo.utils import verificar_token
from werkzeug.security import generate_password_hash
from estudo.forms import AtualizarUsuarioForm, AtualizarLojistaForm  # ou ajuste o nome conforme necessário
from estudo.forms import UserForm, StoreForm

#rotas pedidos
# from flask import Pedidos






@app.route('/')
def homepage():
    if current_user.is_authenticated:
        user_cookie = session.get('_user_id', '')

        if user_cookie.startswith('store:'):
            return redirect(url_for('dashboard_store'))
        
        if user_cookie.startswith('user:'):
            return redirect(url_for('index'))
        
    return render_template('index.html')



#rota para página inicial em todas as páginas
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/index")
def returnbase():
    return render_template('index.html')


@app.route('/login/', methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        login_user(form.user, remember=True)

        # Aqui começa o salvamento do carrinho da sessão
        carrinho_session = session.get('carrinho')
        if carrinho_session:
            # Apaga carrinho antigo do usuário
            carrinho_antigo = Carrinho.query.filter_by(user_id=form.user.id).first()
            if carrinho_antigo:
                db.session.delete(carrinho_antigo)
                db.session.commit()

            # Cria novo carrinho vazio
            carrinho_db = Carrinho(user_id=form.user.id)
            db.session.add(carrinho_db)
            db.session.commit()


            for item_sessao in carrinho_session:
                item_existente = ItemCarrinho.query.filter_by(
                    carrinho_id=carrinho_db.id,
                    nome_produto=item_sessao['nome_produto']
                ).first()

                if item_existente:
                    item_existente.quantidade += item_sessao['quantidade']
                else:
                    novo_item = ItemCarrinho(
                        carrinho_id=carrinho_db.id,
                        nome_produto=item_sessao['nome_produto'],
                        preco=item_sessao['preco'],
                        quantidade=item_sessao['quantidade']
                    )
                    db.session.add(novo_item)

            db.session.commit()
            session.pop('carrinho', None)  # limpa a sessão

        # Aqui termina

        flash('Login realizado com sucesso!', 'success')
        return redirect(url_for('homepage'))

    return render_template('auth/login.html', form=form)


#login para lojistas
@app.route('/login_store/', methods=["GET", "POST"])
def login_store():
    form = LoginStore()

    if form.validate_on_submit():
        login_user(form.store, remember=True)
        flash("Login da loja realizado com sucesso!", "success")
        return redirect(url_for("dashboard_store"))

    return render_template("auth/login_store.html", form=form)


@app.route("/dashboard_store")
@login_required
def dashboard_store():
    # Garante que somente lojas podem acessar
    if not hasattr(current_user, "cnpj"):
        flash("Acesso permitido somente para lojas!", "danger")
        return redirect(url_for("homepage"))

    return render_template("dashboard_store.html", loja=current_user)


@app.route('/meu-carrinho', methods=['GET'])
@login_required
def meu_carrinho():
    carrinho = Carrinho.query.filter_by(user_id=current_user.id).first()
    if not carrinho:
        return jsonify([])

    itens = []
    for item in carrinho.itens:
        itens.append({
            'name': item.nome_produto,
            'price': item.preco,
            'quantity': item.quantidade
        })

    return jsonify(itens)

  



@app.route('/cadastrousuario/',methods=["GET","POST"])
def cadastrousuario():
    form=UserForm()
    if form.validate_on_submit():
        user=form.save()
        login_user(user, remember=True)
        flash('Cadastro realizado com sucesso! Você já está logado. ','success')
        return redirect(url_for('homepage'))


    return render_template('cadastros/cadastrousuario.html', form=form)

@app.route('/sair/')
def logout():
     logout_user()
     flash('Aguardamos você de volta!', 'danger')
     return redirect(url_for('homepage'))




@app.route('/cadastroloja/', methods=["GET","POST"])
def cadastroloja():
     form=StoreForm()
     if form.validate_on_submit():
         loja=form.save()
         login_user(loja, remember=True)
         flash('Cadastro realizado com sucesso! Você já está logado', 'success')
         return redirect(url_for('dashboard_store'))
     
     
     return render_template('cadastros/cadastroloja.html', form=form)
        
# rota de erro
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


#rota para salvar carrinho
@app.route('/adicionar-carrinho', methods=['POST'])
def adicionar_carrinho():
    dados = request.get_json()

    novo_item = {
        'nome_produto': dados.get('nome_produto'),
        'preco': float(dados.get('preco')),
        'quantidade': int(dados.get('quantidade', 1))
    }

    if 'carrinho' not in session:
        session['carrinho'] = []

    # Verifica se já existe o produto no carrinho
    carrinho = session['carrinho']
    for item in carrinho:
        if item['nome_produto'] == novo_item['nome_produto']:
            item['quantidade'] += novo_item['quantidade']
            break
    else:
        carrinho.append(novo_item)

    session['carrinho'] = carrinho
    session.modified = True

    return jsonify({'mensagem': 'Item adicionado ao carrinho'})

#AGORA, IREMOS CRIAR OS PASSOS DE Pedir link de recuperação
 # função que você deve implementar

@app.route('/recuperar-senha', methods=['GET', 'POST'])
def recuperar_senha():
    form = PedidoRecuperacaoForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            token = gerar_token(user.email)
            link = url_for('redefinir_senha', token=token, _external=True)

            # Renderiza o template do e-mail com o link
            corpo_email = render_template('cadastros/email_redefinir_senha.html', link=link)

            enviar_email(user.email, 'Redefinir sua senha', corpo_email)
            flash('Enviamos um link para redefinir sua senha no seu email.', 'info')
            return redirect(url_for('login'))

        else:
            flash('Email não encontrado.', 'warning')
        # return redirect(url_for('login'))
    return render_template('cadastros/recuperar_senha.html', form=form)



# E Página para redefinir senha
@app.route('/redefinir-senha/<token>', methods=['GET', 'POST'])
def redefinir_senha(token):
    email = verificar_token(token)
    if not email:
        flash('O link é inválido ou expirou.', 'danger')
        return redirect(url_for('recuperar_senha'))

    form = RedefinirSenhaForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=email).first()
        if user:
            user.senha = generate_password_hash(form.senha.data)
            db.session.commit()
            flash('Sua senha foi redefinida com sucesso.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Usuário não encontrado.', 'danger')
            return redirect(url_for('recuperar_senha'))

    return render_template('cadastros/redefinir_senha.html', form=form)


#atualizar cadastro

@app.route('/atualizar_cadastro', methods=['GET', 'POST'])
@login_required#server para impedir que alguém edite  os dados de outro usuário ou da loja sem está logado
def atualizar_cadastro():
    form = AtualizarUsuarioForm(obj=current_user)#usado para preencher os dados do usuario

    if form.validate_on_submit():
        # Atualizar os dados
        current_user.nome = form.nome.data
        current_user.sobrenome = form.sobrenome.data
        current_user.email = form.email.data
        current_user.endereco=form.endereco.data
        current_user.complemento=form.complemento.data
        current_user.celular=form.celular.data

        # Atualiza a senha somente se o campo não estiver vazio
        if form.senha.data:
            current_user.senha = generate_password_hash(form.senha.data)

        db.session.commit()
        flash('Seus dados foram atualizados com sucesso!', 'success')
        return redirect(url_for('homepage'))

    return render_template('cadastros/atualizar_cadastro.html', form=form)

@app.route('/atualizar_cadastro_lojista/', methods=['GET', 'POST'])
@login_required#server para impedir que alguém edite  os dados de outro usuário ou da loja sem está logado
def atualizar_cadastro_lojista():
    form=AtualizarLojistaForm(obj=current_user)#usado para preencher os dados do usuario

    if form.validate_on_submit():
        #atualizar os dados da loja
        current_user.nome=form.nome.data
        current_user.sobrenome=form.sobrenome.data
        current_user.email=form.email.data
        current_user.celularp=form.celularp.data
        current_user.nomedaloja=form.nomedaloja.data
        current_user.nextreferencia=form.nextreferencia.data
        current_user.cnpj=form.cnpj.data
        current_user.endereco=form.endereco.data

        #atualizar as senhas somente se o campo não estiver vazio
        if form.senha.data:
            current_user.senha=generate_password_hash(form.senha.data)
        db.session.commit()
        flash('Seus dados foram atualizados com succeso!','success')
        return redirect(url_for('dashboard_store'))
    
    return render_template('cadastros/atualizar_cadastro_lojista.html', form=form)


# rotas para produtos CRUD

# routes_produtos.py (por exemplo)

# from flask import render_template, redirect, url_for, request, flash
# from flask_login import login_required, current_user
# from estudo import db

#rotas de criar, editar, listar e excluir produtos, CRUD
from estudo.models import Produto
from estudo.forms import ProdutoForm
from werkzeug.utils import secure_filename
import os


# ----------------------------
# LISTAR PRODUTOS
# ----------------------------
@app.route('/produtos')
@login_required
def produtos_lista():
    produtos = Produto.query.filter_by(loja_id=current_user.id).all()
    return render_template('produtos/produtos_lista.html', produtos=produtos)



# ----------------------------
# CRIAR PRODUTO
# ----------------------------
@app.route('/produto/novo', methods=['GET', 'POST'])
@login_required
def produto_novo():
    form = ProdutoForm()
    #para salvar a imagem
    if form.validate_on_submit():
        imagem = form.imagem.data
        nome_arquivo = None

        if imagem and imagem.filename:
            nome_arquivo = secure_filename(imagem.filename)

            # cria a pasta se não existir
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

            caminho = os.path.join(app.config['UPLOAD_FOLDER'], nome_arquivo)
            imagem.save(caminho)

        produto = Produto(
            loja_id=current_user.id,
            nome=form.nome.data,
            descricao=form.descricao.data,
            preco=form.preco.data,
            categoria=form.categoria.data,
            ativo=form.ativo.data,
            imagem=nome_arquivo

        )
        db.session.add(produto)
        db.session.commit()
        
        flash("Produto criado com sucesso!", "success")
        return redirect(url_for('produtos_lista'))
    
    return render_template('produtos/produto_form.html', form=form, titulo="Novo Produto")

# ----------------------------
# EDITAR PRODUTO
# ----------------------------

@app.route('/produto/<int:id>/editar', methods=['GET', 'POST'])
@login_required
def produto_editar(id):
    produto = Produto.query.filter_by(
        id=id,
        loja_id=current_user.id
    ).first_or_404()

    form = ProdutoForm()

    # popular campos manualmente (GET)
    if request.method == 'GET':
        form.nome.data = produto.nome
        form.descricao.data = produto.descricao
        form.preco.data = produto.preco
        form.categoria.data = produto.categoria
        form.ativo.data = produto.ativo

    if form.validate_on_submit():
        imagem = form.imagem.data  # AGORA SEMPRE FileStorage ou None

        if imagem and imagem.filename:
            nome_arquivo = secure_filename(imagem.filename)

            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
            caminho = os.path.join(app.config['UPLOAD_FOLDER'], nome_arquivo)

            imagem.save(caminho)
            produto.imagem = nome_arquivo
        # se não enviar imagem nova, mantém a antiga automaticamente

        produto.nome = form.nome.data
        produto.descricao = form.descricao.data
        produto.preco = form.preco.data
        produto.categoria = form.categoria.data
        produto.ativo = form.ativo.data

        db.session.commit()
        flash("Produto atualizado com sucesso!", "success")
        return redirect(url_for('produtos_lista'))

    return render_template(
        'produtos/produto_form.html',
        form=form,
        titulo="Editar Produto"
    )




# ----------------------------
# EXCLUIR PRODUTO
# ----------------------------
@app.route('/produto/<int:id>/excluir', methods=['POST'])
@login_required
def produto_excluir(id):
    produto = Produto.query.filter_by(id=id, loja_id=current_user.id).first_or_404()

    db.session.delete(produto)
    db.session.commit()

    flash("Produto removido com sucesso!", "success")
    return redirect(url_for('produtos_lista'))


# fim das rotas para produtos CRUD

from estudo.models import Pedidos

#inicio das rotas para lojista terem acesso aos status de pedidos
@app.route('/pedidos')
@login_required
def pedidos():
    pedidos= Pedidos.query.filter_by(
        loja_id=current_user.id
    ).order_by(Pedidos.id.desc()).all()

    return render_template('pedidos/lista.html', pedidos=pedidos)

#fim das rotas para lojista terem acesso aos status de pedidos
