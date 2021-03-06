from mysql import connector
import json
import inspect
import jsonpickle
from flaskr.utils.debug import Debug
from flaskr.utils.config import Config

class Banco:
    def __init__(self, tabela:str, entidade):
        self.tabela   = tabela
        self.entidade = entidade
        self.mydb     = connector.connect(
            host      = Config().get('host'),
            user      = Config().get('user'),
            password  = Config().get('password'),
            database  = Config().get('database') )


    def selecionar_obj(self, campos:str='*', where:str='1=1'):
        mycursor = self.mydb.cursor()
        mycursor.execute(
            ' SELECT ' + campos +
            ' FROM   ' + self.tabela +
            ' WHERE  ' + where )
        return self.setar( mycursor.fetchall(), campos )


    def selecionar_json(self, campos:str='*', where:str='1=1'):
        return jsonpickle.encode(
            self.selecionar_obj(campos, where),
            unpicklable=False )


    def selecionar_personalizado(self, sql):
        mycursor = self.mydb.cursor()
        mycursor.execute(sql)
        return mycursor.fetchall()


    def editar(self, campos, where):
        mycursor = self.mydb.cursor()
        sql = (' UPDATE ' + self.tabela +
               ' SET    ' + campos +
               ' WHERE  ' + where )
        mycursor.execute(sql)
        self.mydb.commit()

    
    def deletar(self, id):
        mycursor = self.mydb.cursor()
        sql = (' DELETE FROM ' + self.tabela +
               ' WHERE id = %s' )
        mycursor.execute(sql, (id,) )
        self.mydb.commit()


    def inserir(self, campos, valores):
        mycursor = self.mydb.cursor()
        sql = (' INSERT INTO ' + self.tabela +
               ' (' + campos +')'
               ' VALUES(' + valores +')' )
        mycursor.execute(sql)
        self.mydb.commit()

    
    def deletar_tudo(self):
        return self.deletar('DELETE FROM '+str(self.tabela)+' WHERE id > 0')
            

    def _elemento_por_index(self, elemento, index:int):
        if index >= len(elemento):
            return None
        else:
            return elemento[index]


    def _setar_index(self, linha, qtd_index):
        linhas = []
        for index in range(0, qtd_index):
            linhas.append(
                self._elemento_por_index(linha, index) )
        return tuple(linhas)


    def setar(self, linhas:list, campos:str):
        qtd_index = 0
        if campos == '*':
            qtd_index = (len((inspect.signature(self.entidade.__init__)).parameters) -1)
        else:
            qtd_index = len(campos.split(','))

        objetos = []
        for linha in linhas:
            objeto = self.entidade(
                *self._setar_index(linha, qtd_index) )
            objetos.append( objeto )
        return objetos