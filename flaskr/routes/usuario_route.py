import json
from flask import Flask, jsonify, render_template, request, redirect, url_for, session
from flaskr.controllers.usuario_ctrl import UsuarioCtrl
from flaskr.controllers.controle_acesso_ctrl import ControleAcessoCtrl
from flaskr.daos.usuario_dao import UsuarioDao
from flaskr.daos.grupo_usuario_dao import GrupoUsuarioDao
from flaskr.entities.usuario import Usuario
from flaskr.utils.debug import Debug

class UsuarioRoute:
    def __init__(self, app):
        self._app = app

        self._app.add_url_rule(
            '/usuario/listar',
            'usualio/listar',
            self.listar )

        self._app.add_url_rule(
            '/usuario/novo',
            '/usuario/novo',
            self.novo )

        self._app.add_url_rule(
            '/usuario/<id>/editar',
            '/usuario/id/editar',
            self.editar )

        self._app.add_url_rule(
            '/usuario/<id>/salvar',
            'usuario-id-salvar',
            methods   = ['POST'],
            view_func = self.atualizar )

        self._app.add_url_rule(
            '/usuario/salvar',
            'usuario-salvar',
            methods   = ['POST'],
            view_func = self.inserir )

        self._app.add_url_rule(
            '/usuario/<id>/excluir',
            'usuario-id-excluir',
            methods   = ['GET'],
            view_func = self.deletar )


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


    def inserir(self):
        usuario = request.form.get('usuario')
        grupo   = request.form.get('grupo')
        senha   = request.form.get('senha')

        senha = ControleAcessoCtrl().criar_senha(senha)

        if grupo == None:
            grupo = 1

        UsuarioDao().inserir(
            campos  = 'usuario, senha, id_grupo',
            valores = "'"+usuario+"','"+senha+"',"+str(grupo) )
        return redirect(url_for('usualio/listar'))


    def atualizar(self, id):
        descricao = request.form.get('descricao')
        UsuarioDao().editar(
            campos = ' descricao="'+descricao+'"',
            where  = ' id='+ str(id) )
        return redirect(url_for('usualio/listar'))


    def deletar(self, id):
        GrupoUsuarioDao().deletar(
            id = id )
        return redirect(url_for('usuario/listar') )


    def _campos(self, entidade:Usuario):
        dados_formulario = []
        dados_formulario.append({
            'tag'   : 'input',
            'id'    : 'id',
            'tipo'  : 'text',
            'name'  : 'id',
            'label' : 'Id',
            'value' : entidade.id,
            'class' : 'form-control'
        })
        dados_formulario.append({
            'tag'   : 'input',
            'id'    : 'usuario',
            'tipo'  : 'text',
            'name'  : 'usuario',
            'label' : 'Usuário',
            'value' : entidade.usuario,
            'class' : 'form-control'
        })
        dados_formulario.append({
            'conteudo_tag' : self._itens_grupo(),
            'tag'   : 'select',
            'id'    : 'grupo',
            'tipo'  : 'select',
            'name'  : 'grupo',
            'label' : 'Grupo',
            'value' : None,
            'class' : 'form-select',
        })
        dados_formulario.append({
            'tag'   : 'input',
            'id'    : 'senha',
            'tipo'  : 'password',
            'name'  : 'senha',
            'label' : 'Senha',
            'value' : entidade.senha,
            'class' : 'form-control'
        })
        return dados_formulario


    def _itens_grupo(self):
        options = ''
        for grupo in GrupoUsuarioDao().selecionar_obj():
            options = options + '<option value="'+str(grupo.id)+'">'+grupo.descricao+'</option>'
        return options