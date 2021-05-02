from flask import Flask, jsonify, render_template, request, redirect, url_for, session
from controllers.controle_acesso_ctrl import ControleAcessoCtrl

class LoginRoute:
    def __init__(self, app):
        self._app = app

        self._app.add_url_rule('/',
            'inicial', self.inicial)
        
        self._app.add_url_rule('/login',
            'login', self.login)

        self._app.add_url_rule('/logout',
            'logout', self.logout)

        self._app.add_url_rule('/verificar-login',
            methods=['POST'], view_func=self.verificar_login)


    def inicial(self):
        if 'usuario' in session:
            return render_template('inicial/inicial.html', titulo='Inicial')
        return redirect(url_for('login'))

    
    def login(self):
        if 'usuario' in session:
            return redirect(url_for('inicial'))
        return render_template('login/login.html', titulo='Login')

    
    def logout(self):
        session.clear()
        return redirect(url_for('login'))


    def verificar_login(self):
        usuario = request.form.get('usuario')
        senha   = request.form.get('senha')
        if ControleAcessoCtrl().verificar_usuario_senha(usuario, senha):
            session['usuario'] = usuario
            session['senha']   = senha
            return redirect(url_for('inicial'))
        return redirect(url_for('login'))