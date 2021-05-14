import json
from flask import Blueprint, render_template, request, redirect, url_for
from flaskr.daos.usuario_grupo_dao import UsuarioGrupoDao
from flaskr.entities.usuario_grupo import UsuarioGrupo
from flaskr.utils.debug import Debug

bp  = Blueprint(
    'usuario-grupo',
    __name__,
    template_folder='templates' )

class UsuarioGrupoCtrl:
    @bp.route('/usuario/grupo/listar')
    def listar():
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


    @bp.route('/usuario/grupo/novo')
    def novo():
        return render_template('formulario_padrao.html',
            dados  = UsuarioGrupoCtrl._campos(UsuarioGrupo()),
            titulo = 'Novo Grupo de Usuários' )


    @bp.route('/usuario/grupo/<id>/editar')
    def editar(id):
        dados_grupo = UsuarioGrupoDao().selecionar_obj(
            where =' id = '+ str(id) )

        grupo = dados_grupo[0]
        return render_template('formulario_padrao.html',
            dados  = UsuarioGrupoCtrl._campos(grupo),
            titulo = 'Editar Grupo de Usuários' )


    @bp.route('/usuario/grupo/salvar')
    def inserir():
        descricao = request.form.get('descricao')
        UsuarioGrupoDao().inserir(
            campos  = 'descricao',
            valores = "'"+descricao+"'" )
        return redirect(url_for('usuario/grupo/listar'))


    @bp.route('/usuario/grupo/<id>/salvar')
    def atualizar(id):
        descricao = request.form.get('descricao')
        UsuarioGrupoDao().editar(
            campos = ' descricao="'+descricao+'"',
            where  = ' id='+ str(id) )
        return redirect(url_for('usuario/grupo/listar'))


    @bp.route('/usuario/grupo/<id>/excluir')
    def deletar(id):
        UsuarioGrupoDao().deletar(
            id = id )
        return redirect(url_for('usuario/grupo/listar'))


    def _campos(entidade):
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