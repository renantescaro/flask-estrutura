from flask import Flask
from flaskr.controllers.login_ctrl import bp as bp_login
from flaskr.controllers.usuario_ctrl import bp as bp_usuario
from flaskr.controllers.usuario_grupo_ctrl import bp as bp_usuario_grupo

def create_app(test_config=None):
    app = Flask(__name__, 
        static_url_path = '/static',
        static_folder   = 'static',
        instance_relative_config = True )

    app.config.from_mapping(
        SECRET_KEY   = 'super secret key',
        SESSION_TYPE = 'filesystem',
        JSONIFY_PRETTYPRINT_REGULAR = False )

    app.register_blueprint(bp_login)
    app.register_blueprint(bp_usuario)
    app.register_blueprint(bp_usuario_grupo)

    return app