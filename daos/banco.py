from mysql import connector
import inspect

class Banco:
    def __init__(self, tabela, entidade):
        self.tabela   = tabela
        self.entidade = entidade
        self.mydb     = connector.connect(
            host     = "localhost",
            user     = "root",
            password = "",
            database = "teste")


    def selecionar(self, campos='*', where='1=1'):
        mycursor = self.mydb.cursor()
        mycursor.execute(
            ' SELECT ' + str(campos)      +
            ' FROM '   + str(self.tabela) +
            ' WHERE '  + str(where)       

        )
        return mycursor.fetchall()


    def executar(self):
        pass


    def selecionar_tudo(self):
        return self.selecionar('SELECT * FROM '+str(self.tabela))

    
    def deletar_tudo(self):
        return self.deletar('DELETE FROM '+str(self.tabela)+' WHERE id > 0')
            

    def elemento_por_index(self, elemento, index):
        if index >= len(elemento):
            return None
        else:
            return elemento[index]


    def setar_index(self, linha, qtd_index):
        linhas = []
        for index in range(0, qtd_index):
            linhas.append( 
                self.elemento_por_index(linha, index) )
        return tuple(linhas)


    def setar(self, linhas):
        qtd_index = (len((inspect.signature(self.entidade.__init__)).parameters) -1)
        objetos = []
        for linha in linhas:
            objeto = self.entidade(
                *self.setar_index(linha, qtd_index) )
            objetos.append( objeto )
        return objetos