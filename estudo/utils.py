# redefinir senhas
#  a biblioteca itsdangerous (já padrão com Flask) para criar tokens com expiração.
from itsdangerous import URLSafeTimedSerializer
from flask import current_app

# validaçao de email
# você precisa instalar o Flask-Mail para poder enviar e-mails com Flask.
# pip install Flask-Mail

from flask_mail import Message
from flask import render_template
from estudo import mail  # ou de onde estiver importado o objeto `mail`

def gerar_token(email):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    return serializer.dumps(email, salt='recuperar-senha')

def verificar_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    try:
        email = serializer.loads(token, salt='recuperar-senha', max_age=expiration)
    except Exception:
        return None
    return email


def enviar_email(destinatario, assunto, corpo_html):
    msg = Message(
        subject=assunto,
        sender=current_app.config.get('MAIL_DEFAULT_SENDER', 'seuemail@gmail.com'),
        recipients=[destinatario]
    )
    msg.html = corpo_html
    mail.send(msg)


