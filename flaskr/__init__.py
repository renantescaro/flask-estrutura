from flask import Flask, render_template, jsonify, url_for, send_file, redirect, session, request
from flaskr.routes.rotas import Rotas

def create_app(test_config=None):
    app = Flask(__name__, 
        static_url_path = '/static',
        static_folder   = 'static',
        instance_relative_config = True )

    app.config.from_mapping(
        SECRET_KEY   = 'super secret key',
        SESSION_TYPE = 'filesystem',
        JSONIFY_PRETTYPRINT_REGULAR = False
    )
    Rotas(app)
    return app