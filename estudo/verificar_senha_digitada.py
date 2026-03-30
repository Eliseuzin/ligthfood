import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from werkzeug.security import check_password_hash
from estudo import app
from estudo.models import User

senha_do_usuario = "12345"

with app.app_context():
    user = User.query.filter_by(email="vin1zitoow@gmail.com").first()
    if user:
        hash_salvo = user.senha  # o valor salvo no banco
        if check_password_hash(hash_salvo, senha_do_usuario):
            print("Senha correta!")
        else:
            print("Senha incorreta!")
    else:
        print("Usuário não encontrado")


# from werkzeug.security import generate_password_hash, check_password_hash
# # Gerar hash
# hash = generate_password_hash("minha_senha", method='scrypt')
# # Verificar senha
# check_password_hash(hash, "minha_senha")  # True
