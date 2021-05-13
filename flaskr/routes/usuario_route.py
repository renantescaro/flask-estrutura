from flaskr.controllers.usuario_ctrl import UsuarioCtrl

class UsuarioRoute:
    def __init__(self, app):
        self._app = app

        self._app.add_url_rule(
            '/usuario/listar',
            'usualio/listar',
            UsuarioCtrl().listar )

        self._app.add_url_rule(
            '/usuario/novo',
            '/usuario/novo',
            UsuarioCtrl().novo )

        self._app.add_url_rule(
            '/usuario/<id>/editar',
            '/usuario/id/editar',
            UsuarioCtrl().editar )

        self._app.add_url_rule(
            '/usuario/<id>/salvar',
            'usuario-id-salvar',
            methods   = ['POST'],
            view_func = UsuarioCtrl().atualizar )

        self._app.add_url_rule(
            '/usuario/salvar',
            'usuario-salvar',
            methods   = ['POST'],
            view_func = UsuarioCtrl().inserir )

        self._app.add_url_rule(
            '/usuario/<id>/excluir',
            'usuario-id-excluir',
            methods   = ['GET'],
            view_func = UsuarioCtrl().deletar )