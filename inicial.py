from flask import Flask, render_template, jsonify, url_for, send_file, redirect, session, request
from controllers.usuario_ctrl import UsuarioCtrl

app = Flask('api_tray', static_url_path='/static', static_folder='static')


# pagina inicial
@app.route('/', methods=['GET'])
def inicial():
    if 'usuario' in session:
        return render_template('inicial/inicial.html', titulo='Página Inicial')
    return redirect(url_for('login'))


# pagina login
@app.route('/login', methods=['GET'])
def login():
    if 'usuario' in session:
        return redirect(url_for('inicial'))
    return render_template('login/login.html', titulo='Login')


# logout
@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return render_template('login/login.html', titulo='Login')


# verifica dados da página login
@app.route('/verificar-login', methods=['POST'])
def verificar_login():
    usuario = request.form.get('usuario')
    senha   = request.form.get('senha')
    if UsuarioCtrl().verificar_usuario_senha(usuario, senha):
        session['usuario'] = usuario
        session['senha']  = senha
        return redirect(url_for('inicial'))
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(port=5000, debug=True, host='0.0.0.0')