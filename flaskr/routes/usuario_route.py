import json
from flask import Flask, jsonify, render_template, request, redirect, url_for, session
from flaskr.controllers.usuario_ctrl import UsuarioCtrl
from flaskr.daos.usuario_dao import UsuarioDao
from flaskr.entities.usuario import Usuario

class UsuarioRoute:
    def __init__(self, app):
        self._app = app

        self._app.add_url_rule(
            '/usuario/listar',
            'usualio/listar', self.listar)

        self._app.add_url_rule(
            '/usuario/novo',
            '/usuario/novo',
            self.novo )

        self._app.add_url_rule(
            '/usuario/<id>/editar',
            '/usuario/id/editar',
            self.editar)


    def listar(self):
        return render_template(
            'usuario/listagem.html',
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


    def novo(self):
        return render_template(
            'formulario_padrao.html',
            dados  = self._campos(Usuario()),
            titulo = 'Novo Usuário' )

    
    def editar(self, id):
        dados_formulario = []
        dados_usuario    = UsuarioDao().selecionar_obj(
            where=' id = '+ str(id) )

        return render_template(
            'formulario_padrao.html',
            dados  = self._campos(dados_usuario[0]),
            titulo = 'Editar Usuário' )


    def _campos(self, entidade:Usuario):
        dados_formulario = []
        dados_formulario.append({
            'id'    : 'id',
            'tipo'  : 'text',
            'name'  : 'id',
            'label' : 'Id',
            'value' : entidade.id
        })
        dados_formulario.append({
            'id'    : 'usuario',
            'tipo'  : 'text',
            'name'  : 'usuario',
            'label' : 'Usuário',
            'value' : entidade.usuario
        })
        dados_formulario.append({
            'id'    : 'grupo',
            'tipo'  : 'select',
            'name'  : 'grupo',
            'label' : 'Grupo',
            'value' : ''
        })
        dados_formulario.append({
            'id'    : 'senha',
            'tipo'  : 'password',
            'name'  : 'senha',
            'label' : 'Senha',
            'value' : entidade.senha
        })
        return dados_formulario