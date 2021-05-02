from flask import Flask, jsonify, render_template, request, redirect, url_for, session
from daos.grupo_usuario_dao import GrupoUsuarioDao

class GrupoUsuarioRoute:
    def __init__(self, app):
        self._app = app

        self._app.add_url_rule('/grupo-usuario/listar',
            'grupo-usuario/listar', self.listar)


    def listar(self):
        return render_template('grupo-usuario/listagem.html',
            dados  = GrupoUsuarioDao().selecionar_json(),
            titulo = 'Listagem de Grupos')