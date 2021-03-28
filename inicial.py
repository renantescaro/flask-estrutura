from flask import Flask, render_template, jsonify, url_for, send_file

app = Flask('api_tray', static_url_path='/static', static_folder='static')

@app.route('/', methods=['GET'])
def inicial():
    return render_template('inicial/inicial.html', titulo='Página Inicial')

@app.route('/login', methods=['GET'])
def login():
    return render_template('login/login.html')

if __name__ == "__main__":
    app.run(port=5000, debug=True, host='0.0.0.0')