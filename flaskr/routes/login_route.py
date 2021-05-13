from flaskr.controllers.login_ctrl import LoginCtrl

class LoginRoute:
    def __init__(self, app):
        self._app = app

        self._app.add_url_rule(
            '/',
            'inicial',
            LoginCtrl().inicial )
        
        self._app.add_url_rule(
            '/login',
            'login',
            LoginCtrl().login )

        self._app.add_url_rule(
            '/logout',
            'logout',
            LoginCtrl().logout )

        self._app.add_url_rule(
            '/verificar-login',
            methods=['POST'],
            view_func=LoginCtrl().verificar_login )