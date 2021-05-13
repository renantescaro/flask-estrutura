import json
from flaskr.daos.banco import Banco
from flaskr.entities.usuario_grupo import UsuarioGrupo

class UsuarioGrupoDao(Banco):
    def __init__(self):
        self.tabela   = 'usuario_grupo'
        self.entidade = UsuarioGrupo
        super().__init__(
            self.tabela,
            self.entidade)


    def selecionar_por_id(self, id):
        return self.setar(
            linhas = self.selecionar(where='id='+str(id)) )