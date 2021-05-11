import sys
sys.path.append('C:\\Users\\renan.tescaro\\Desktop\\flask\\flask-estrutura\\')

from flaskr.controllers.controle_acesso_ctrl import ControleAcessoCtrl


senha = ControleAcessoCtrl().criar_senha('123')
print(senha)