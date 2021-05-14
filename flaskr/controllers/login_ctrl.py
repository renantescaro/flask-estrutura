from flask import Blueprint, render_template, request, redirect, url_for, session
from flaskr.controllers.controle_acesso_ctrl import ControleAcessoCtrl

bp  = Blueprint(
    'login',
    __name__,
    template_folder='templates' )

class LoginCtrl:
    @bp.route('/')
    def inicial():
        if 'usuario' in session:
            return render_template('inicial/inicial.html', titulo='Inicial')
        return redirect(url_for('login'))


    @bp.route('/login')
    def login():
        if 'usuario' in session:
            return redirect(url_for('inicial'))
        return render_template('login/login.html', titulo='Login')


    @bp.route('/logout')
    def logout():
        session.clear()
        return redirect(url_for('login'))


    @bp.route('/verificar-login')
    def verificar_login():
        usuario = request.form.get('usuario')
        senha   = request.form.get('senha')
        if ControleAcessoCtrl().verificar_usuario_senha(usuario, senha):
            session['usuario'] = usuario
            session['senha']   = senha
            return redirect(url_for('inicial'))
        return redirect(url_for('login') )