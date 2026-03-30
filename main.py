from estudo import app
from estudo.utils import gerar_token, verificar_token, enviar_email
#rodar o projeto, apenas quem estiver chamando main
if __name__=="__main__":
  #sempre que acontecer uma mudança ele estará iniciando novamente
  app.run(debug=True)
  



# 1️⃣ app.run() bloqueia a execução
# ➡️ Tudo que vem depois dele não roda enquanto o servidor está ativo.


#  Criar o ambiente virtual
# No seu terminal (cmd), execute:


#digitar 'dir' para conferir se a pasta venv existir
#A pasta venv tem que aparecer no projeto, caso contrário execute:
# python -m venv venv

#Caso de erro indica que você está tentando executar o comando de ativação do ambiente virtual no PowerShell, mas está usando a sintaxe de outro terminal (cmd).
 
#PARA COMANDO CMD

#python -m venv venv para criar o ambiente virtual
#  ativar o ambiente virtual

# 
# Desativar o ambiente virtual (quando terminar)
# deactivate

#caso de um erro como: não pode ser carregado porque a execução de scripts foi desabilitada neste sistema. Temos que alterar a política de execução apenas para a sessão atual utilizando o camando:
#Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

#depois ativa utilizando: .\venv\Scripts\Activate.ps1

#  No PowerShell(mais comum hoje em dia), o comando correto é:
# .\venv\Scripts\Activate.ps1

# pip show flask-wtf
# verificar a situçao do flask_wtf instalado
 
# Pressione Ctrl + Shift + P
# Digite: Reload Window e execute
# as vezes ajudar a corrigir problemas de importação

#  Isso vai automaticamente envolver o conteúdo selecionado dentro de uma <div>.
# Emmet: Wrap with Abbreviation


# O shell interativo do Python é um ambiente onde você pode digitar
#  e executar comandos Python linha por linha. Ele aparece quando 
# você digita python (ou python3, em alguns casos) no terminal.

# Quando terminar, digite:
# exit()


# from estudo import app, db
# from estudo.models import User

# with app.app_context():
#     total = User.query.delete()
#     db.session.commit()
#     print(f"{total} usuários apagados.")


#exs. de commits

#git add requirements.txt
#git commit -m "adicionando requirements.txt"
#git push