import json
from flask import Flask, jsonify, render_template, request, redirect, url_for, session
from flaskr.daos.usuario_grupo_dao import UsuarioGrupoDao
from flaskr.entities.usuario_grupo import UsuarioGrupo
from flaskr.utils.debug import Debug

class UsuarioGrupoCtrl:
    def listar(self):
        return render_template(
            'listagem_padrao.html',
            dados  = UsuarioGrupoDao().selecionar_json(),
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
            dados  = self._campos(UsuarioGrupo()),
            titulo = 'Novo Grupo de Usuários' )


    def editar(self, id):
        dados_grupo = UsuarioGrupoDao().selecionar_obj(
            where =' id = '+ str(id) )

        grupo = dados_grupo[0]
        return render_template('formulario_padrao.html',
            dados  = self._campos(grupo),
            titulo = 'Editar Grupo de Usuários' )


    def inserir(self):
        descricao = request.form.get('descricao')
        UsuarioGrupoDao().inserir(
            campos  = 'descricao',
            valores = "'"+descricao+"'" )
        return redirect(url_for('usuario/grupo/listar'))


    def atualizar(self, id):
        descricao = request.form.get('descricao')
        UsuarioGrupoDao().editar(
            campos = ' descricao="'+descricao+'"',
            where  = ' id='+ str(id) )
        return redirect(url_for('usuario/grupo/listar'))


    def deletar(self, id):
        UsuarioGrupoDao().deletar(
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