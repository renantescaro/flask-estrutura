from flask import Flask, Response
from flaskr.routes.login_route import LoginRoute
from flaskr.routes.usuario_route import UsuarioRoute
from flaskr.routes.usuario_grupo_route import UsuarioGrupoRoute

class Rotas:
    def __init__(self, app):
        self._app = app
        self._iniciar_rotas()

    
    def _iniciar_rotas(self):
        LoginRoute(self._app)
        UsuarioGrupoRoute(self._app)
        UsuarioRoute(self._app)