from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from datetime import date
from app import db
from app.rotinas import bp
from app.forms import RotinaForm
from app.models import Rotina, ExecucaoDiaria

@bp.route('/')
@login_required
def listar():
    rotinas = Rotina.query.filter_by(usuario_id=current_user.id).order_by(Rotina.titulo).all()
    return render_template('rotinas/listar.html', rotinas=rotinas)

@bp.route('/criar', methods=['GET', 'POST'])
@login_required
def criar():
    form = RotinaForm()
    if form.validate_on_submit():
        rotina = Rotina(
            titulo=form.titulo.data,
            descricao=form.descricao.data,
            ativa=form.ativa.data,
            usuario_id=current_user.id,
            categoria_id=form.categoria_id.data
        )
        db.session.add(rotina)
        db.session.commit()
        flash('Rotina criada!')
        return redirect(url_for('rotinas.listar'))
    return render_template('rotinas/criar.html', form=form)

@bp.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar(id):
    rotina = Rotina.query.get_or_404(id)
    if rotina.usuario_id != current_user.id:
        flash('Acesso negado.')
        return redirect(url_for('rotinas.listar'))
    form = RotinaForm(obj=rotina)
    if form.validate_on_submit():
        rotina.titulo = form.titulo.data
        rotina.descricao = form.descricao.data
        rotina.ativa = form.ativa.data
        rotina.categoria_id = form.categoria_id.data
        db.session.commit()
        flash('Rotina atualizada!')
        return redirect(url_for('rotinas.listar'))
    return render_template('rotinas/editar.html', form=form, rotina=rotina)

@bp.route('/excluir/<int:id>')
@login_required
def excluir(id):
    rotina = Rotina.query.get_or_404(id)
    if rotina.usuario_id != current_user.id:
        flash('Acesso negado.')
        return redirect(url_for('rotinas.listar'))
    db.session.delete(rotina)
    db.session.commit()
    flash('Rotina excluída.')
    return redirect(url_for('rotinas.listar'))

@bp.route('/executar/<int:id>')
@login_required
def executar(id):
    rotina = Rotina.query.get_or_404(id)
    if rotina.usuario_id != current_user.id:
        flash('Acesso negado.')
        return redirect(url_for('rotinas.listar'))
    hoje = date.today()
    if not rotina.ativa:
        flash('Rotina inativa.', 'warning')
        return redirect(url_for('rotinas.listar'))
    if ExecucaoDiaria.query.filter_by(rotina_id=id, usuario_id=current_user.id, data=hoje).first():
        flash('Já executada hoje.', 'info')
        return redirect(url_for('rotinas.listar'))
    execucao = ExecucaoDiaria(rotina_id=id, usuario_id=current_user.id)
    db.session.add(execucao)
    db.session.commit()
    flash('Executada com sucesso!', 'success')
    return redirect(url_for('rotinas.listar'))