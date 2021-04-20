import json
from daos.banco import Banco
from entities.usuario import Usuario

class UsuarioDao(Banco):
    def __init__(self):
        self.tabela   = 'usuario'
        self.entidade = Usuario
        super().__init__(
            self.tabela,
            self.entidade)


    def selecionar_nomes(self):
        return self.setar(
            linhas = self.selecionar(campos='id, nome') )


    def selecionar_por_id(self, id):
        return self.setar(
            linhas = self.selecionar(where='id='+str(id)) )