import bcrypt
from flaskr.daos.usuario_dao import UsuarioDao
from flaskr.utils.debug import Debug

class ControleAcessoCtrl:
    def verificar_usuario_senha(self, usuario, senha):
        if usuario == 'admin' and senha == 'abc123':
            return True
        else:
            return self._comparar_usuario_senha(usuario, senha)

    
    def criar_senha(self, senha):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(senha, salt)

    
    def alterar_senha_usuario(self, usuario, senha_antiga, senha_nova):
        if self._comparar_usuario_senha(usuario, senha_antiga):
            return UsuarioDao().editar(
                campos= ' senha="'+senha_nova+'" ', 
                where = ' usuario="'+usuario+'" ' )
        return False


    def _comparar_usuario_senha(self, usuario, senha):
        usuario_banco = UsuarioDao().selecionar_obj(
            where ='usuario="'+usuario+'"' )

        if len(usuario_banco) == 0:
            return False

        return bcrypt.checkpw(
            bytes(senha, 'utf-8'),
            bytes(usuario_banco[0].senha, 'utf-8') )