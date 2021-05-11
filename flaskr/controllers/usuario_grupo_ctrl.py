import json
from flask import Flask, jsonify, render_template, request, redirect, url_for, session
from flaskr.daos.grupo_usuario_dao import GrupoUsuarioDao
from flaskr.entities.gupo_usuario import GrupoUsuario
from flaskr.utils.debug import Debug

class UsuarioGrupoCtrl:
    def listar(self):
        return render_template(
            'listagem_padrao.html',
            dados  = GrupoUsuarioDao().selecionar_json(),
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
            titulo = 'Listagem de Grupos de Usuários' )


    def novo(self):
        return render_template('formulario_padrao.html',
            dados  = self._campos(GrupoUsuario()),
            titulo = 'Novo Grupo de Usuários' )


    def editar(self, id):
        dados_grupo = GrupoUsuarioDao().selecionar_obj(
            where =' id = '+ str(id) )

        grupo = dados_grupo[0]
        return render_template('formulario_padrao.html',
            dados  = self._campos(grupo),
            titulo = 'Editar Grupo de Usuários' )

    
    def inserir(self):
        descricao = request.form.get('descricao')
        GrupoUsuarioDao().inserir(
            campos  = 'descricao',
            valores = "'"+descricao+"'" )
        return redirect(url_for('usuario/grupo/listar'))

    
    def atualizar(self, id):
        descricao = request.form.get('descricao')
        GrupoUsuarioDao().editar(
            campos = ' descricao="'+descricao+'"',
            where  = ' id='+ str(id) )
        return redirect(url_for('usuario/grupo/listar'))


    def deletar(self, id):
        GrupoUsuarioDao().deletar(
            id = id )
        return redirect(url_for('usuario/grupo/listar'))


    def _campos(self, entidade):
        dados_formulario = []
        dados_formulario.append({
            'tag'   : 'input',
            'id'    : 'id',
            'tipo'  : 'text',
            'name'  : 'id',
            'label' : 'Id',
            'class' : 'form-control',
            'value' : entidade.id })

        dados_formulario.append({
            'tag'   : 'input',
            'id'    : 'descricao',
            'tipo'  : 'text',
            'name'  : 'descricao',
            'label' : 'Descrição',
            'class' : 'form-control',
            'value' : entidade.descricao })
        return dados_formulario