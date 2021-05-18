import json
from flaskr.daos.banco import Banco
from flaskr.entities.usuario import Usuario
from flaskr.utils.debug import Debug

class UsuarioDao(Banco):
    def __init__(self):
        self.tabela   = 'usuario'
        self.entidade = Usuario
        super().__init__(
            self.tabela,
            self.entidade )


    def selecionar_nomes(self):
        return self.setar(
            linhas = self.selecionar(campos='id, nome') )


    def selecionar_por_id(self, id):
        return self.setar(
            linhas = self.selecionar(where='id='+str(id)) )


    def selecionar_com_grupo_json(self):
        sql = """
            SELECT u.id, u.usuario, g.descricao AS grupo 
            FROM usuario AS u
            INNER JOIN usuario_grupo AS g
            ON u.id_grupo = g.id
            """
        usuario_json = []
        for usuario in self.selecionar_personalizado(sql):
            usuario_json.append({
                'id'     : usuario[0],
                'usuario': usuario[1],
                'grupo'  : usuario[2] })
        return json.dumps(usuario_json)