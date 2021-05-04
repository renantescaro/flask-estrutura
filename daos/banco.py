from mysql import connector
import json
import inspect
import jsonpickle
from utils.debug import Debug

class Banco:
    def __init__(self, tabela:str, entidade):
        self.tabela   = tabela
        self.entidade = entidade
        self.mydb     = connector.connect(
            host      = "localhost",
            user      = "root",
            password  = "",
            database  = "teste")


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


    def executar(self):
        pass

    
    def editar(self, campos, where):
        mycursor = self.mydb.cursor()
        sql = (' UPDATE ' + self.tabela +
               ' SET    ' + campos +
               ' WHERE  ' + where )
        mycursor.execute(sql)
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