from flask import Flask, jsonify, render_template, request, redirect, url_for, session
from flaskr.controllers.controle_acesso_ctrl import ControleAcessoCtrl

class LoginCtrl:
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
        return redirect(url_for('login') )