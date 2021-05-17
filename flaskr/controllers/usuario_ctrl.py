import json
from flask import Blueprint, render_template, request, redirect, url_for
from flaskr.controllers.controle_acesso_ctrl import ControleAcessoCtrl
from flaskr.daos.usuario_dao import UsuarioDao
from flaskr.daos.usuario_grupo_dao import UsuarioGrupoDao
from flaskr.entities.usuario import Usuario
from flaskr.utils.debug import Debug

bp  = Blueprint(
    'usuario',
    __name__,
    template_folder='templates' )

class UsuarioCtrl:
    @bp.route('/usuario/listar')
    def listar():
        return render_template(
            'usuario/listagem.html',
            dados  = UsuarioDao().selecionar_com_grupo_json(),
            chaves = json.dumps([
                {
                    'campo'  : 'id',
                    'titulo' : 'Id',
                    'busca'  : 'input'
                },{
                    'campo'  : 'usuario',
                    'titulo' : 'Usuário',
                    'busca'  : 'input'
                },{
                    'campo'  : 'grupo',
                    'titulo' : 'Grupo',
                    'busca'  : 'input'
                } ]),
            titulo = 'Listagem de Usuários')


    @bp.route('/usuario/novo')
    def novo():
        return render_template(
            'formulario_padrao.html',
            dados  = UsuarioCtrl._campos(Usuario()),
            titulo = 'Novo Usuário' )

    @bp.route('/usuario/<id>/editar')
    def editar(id):
        dados_usuario = UsuarioDao().selecionar_obj(
            where=' id = '+ str(id) )

        return render_template(
            'formulario_padrao.html',
            dados  = UsuarioCtrl._campos(dados_usuario[0]),
            titulo = 'Editar Usuário' )


    @bp.route('/usuario/salvar', methods=['POST'])
    def inserir():
        usuario = request.form.get('usuario')
        grupo   = request.form.get('grupo')
        senha   = request.form.get('senha')

        senha = ControleAcessoCtrl().criar_senha(senha)

        if grupo == None:
            grupo = 1

        UsuarioDao().inserir(
            campos  = 'usuario, senha, id_grupo',
            valores = "'"+usuario+"','"+senha+"',"+str(grupo) )
        return redirect('/usuario/listar')


    @bp.route('/usuario/<id>/salvar', methods=['POST'])
    def atualizar(id):
        descricao = request.form.get('descricao')
        UsuarioDao().editar(
            campos = ' descricao="'+descricao+'"',
            where  = ' id='+ str(id) )
        return redirect('/usuario/listar')


    @bp.route('/usuario/<id>/excluir')
    def deletar(id):
        UsuarioDao().deletar(
            id = id )
        return redirect('/usuario/listar' )


    def _campos(entidade:Usuario):
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
            'itens' : UsuarioCtrl._itens_grupo(),
            'tag'   : 'select',
            'id'    : 'grupo',
            'tipo'  : 'select',
            'name'  : 'grupo',
            'label' : 'Grupo',
            'value' : entidade.grupo,
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


    def _itens_grupo():
        options = []
        for grupo in UsuarioGrupoDao().selecionar_obj():
            options.append( { 'valor':grupo.id, 'descricao':grupo.descricao } )
        return options