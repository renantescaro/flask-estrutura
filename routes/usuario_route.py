import json
from flask import Flask, jsonify, render_template, request, redirect, url_for, session
from controllers.usuario_ctrl import UsuarioCtrl
from daos.usuario_dao import UsuarioDao

class UsuarioRoute:
    def __init__(self, app):
        self._app = app

        self._app.add_url_rule('/usuario/listar',
            'usualio/listar', self.listar)

        self._app.add_url_rule(
            '/usuario/<id>/editar',
            '/usuario/id/editar',
            self.editar)


    def listar(self):
        return render_template('usuario/listagem.html',
            dados  = UsuarioDao().selecionar_json('id, usuario'),
            chaves = json.dumps([
                {
                    'campo'  : 'id',
                    'titulo' : 'Id',
                    'busca'  : 'input'
                },{
                    'campo'  : 'usuario',
                    'titulo' : 'Usuário',
                    'busca'  : 'input'
                } ]),
            titulo = 'Listagem de Usuários')

    
    def editar(self, id):
        dados_formulario = []
        dados_usuario    = UsuarioDao().selecionar_obj(
            where=' id = '+ str(id) )

        usuario = dados_usuario[0]
        dados_formulario.append({
            'id'    : 'id',
            'tipo'  : 'text',
            'name'  : 'id',
            'label' : 'Id',
            'value' : usuario.id
        })
        dados_formulario.append({
            'id'    : 'usuario',
            'tipo'  : 'text',
            'name'  : 'usuario',
            'label' : 'Usuário',
            'value' : usuario.usuario
        })
        dados_formulario.append({
            'id'    : 'senha',
            'tipo'  : 'text',
            'name'  : 'senha',
            'label' : 'Senha',
            'value' : usuario.senha
        })

        return render_template('formulario_padrao.html',
            dados  = dados_formulario,
            titulo = 'Editar Usuário' )