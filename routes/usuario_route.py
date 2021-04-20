import json
import collections
from flask import Flask, jsonify, render_template, request, redirect, url_for, session
from controllers.usuario_ctrl import UsuarioCtrl
from daos.usuario_dao import UsuarioDao

class UsuarioRoute:
    def __init__(self, app):
        self._app = app

        self._app.add_url_rule('/usuario/listar',
            'usualio/listar', self.listar)


    def listar(self):
        usuarios =  UsuarioDao().selecionar_json()
        return render_template('usuario/listagem.html',
            dados  = usuarios,
            titulo = 'Listagem de Usuarios')