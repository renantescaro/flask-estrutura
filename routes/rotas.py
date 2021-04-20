from flask import Flask, Response
from routes.login_route import LoginRoute
from routes.usuario_route import UsuarioRoute

class Rotas:
    def __init__(self, app):
        self._app = app
        self._iniciar_rotas()

    
    def _iniciar_rotas(self):
        LoginRoute(self._app)
        UsuarioRoute(self._app)