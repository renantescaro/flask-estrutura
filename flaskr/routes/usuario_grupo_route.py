from flaskr.controllers.usuario_grupo_ctrl import UsuarioGrupoCtrl

class UsuarioGrupoRoute:
    def __init__(self, app):
        self._app = app

        self._app.add_url_rule(
            '/usuario/grupo/listar',
            'usuario/grupo/listar',
            UsuarioGrupoCtrl().listar() )

        self._app.add_url_rule(
            '/usuario/grupo/<id>/editar',
            '/usuario/grupo/id/editar',
            UsuarioGrupoCtrl().editar() )

        self._app.add_url_rule(
            '/usuario/grupo/novo',
            '/usuario/grupo/novo',
            UsuarioGrupoCtrl().novo() )

        self._app.add_url_rule(
            '/usuario/grupo/salvar',
            'usuario-grupo-salvar',
            methods   = ['POST'],
            view_func = UsuarioGrupoCtrl().inserir() )
        
        self._app.add_url_rule(
            '/usuario/grupo/<id>/salvar',
            'usuario-grupo-id-salvar',
            methods   = ['POST'],
            view_func = UsuarioGrupoCtrl().atualizar() )
        
        self._app.add_url_rule(
            '/usuario/grupo/<id>/excluir',
            'usuario-grupo-id-excluir',
            methods   = ['GET'],
            view_func = UsuarioGrupoCtrl().deletar() )