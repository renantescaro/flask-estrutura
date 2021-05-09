from flask import Flask, render_template, jsonify, url_for, send_file, redirect, session, request
from flaskr.routes.rotas import Rotas

app = Flask('app_flask', static_url_path='/static', static_folder='static')    
Rotas(app)

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
    app.run(port=5000, debug=True, host='0.0.0.0')