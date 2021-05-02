import json
from daos.banco import Banco
from entities.gupo_usuario import GrupoUsuario

class GrupoUsuarioDao(Banco):
    def __init__(self):
        self.tabela   = 'grupo_usuario'
        self.entidade = GrupoUsuario
        super().__init__(
            self.tabela,
            self.entidade)


    def selecionar_por_id(self, id):
        return self.setar(
            linhas = self.selecionar(where='id='+str(id)) )