import os
from dotenv import load_dotenv

class Config:
    def arquivo_vazio(self):
        return os.stat(".env").st_size == 0


    def limpar(self):
        open('.env', 'w').close()


    def set(self, hash, valor):
        if Config.get(hash) == None:
            f = open(".env", "a")
            f.write(str(hash).upper()+"="+str(valor)+"\n")
            f.close()


    def get(self, hash):
        load_dotenv()
        return os.getenv(str(hash).upper())