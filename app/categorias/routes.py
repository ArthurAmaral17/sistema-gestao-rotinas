from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from app import db
from app.categorias import bp
from app.forms import CategoriaForm
from app.models import Categoria

@bp.route('/')
@login_required
def listar():
    categorias = Categoria.query.order_by(Categoria.nome).all()
    return render_template('categorias/listar.html', categorias=categorias)

@bp.route('/criar', methods=['GET', 'POST'])
@login_required
def criar():
    form = CategoriaForm()
    if form.validate_on_submit():
        db.session.add(Categoria(nome=form.nome.data))
        db.session.commit()
        flash('Categoria criada!')
        return redirect(url_for('categorias.listar'))
    return render_template('categorias/criar.html', form=form)

@bp.route('/excluir/<int:id>')
@login_required
def excluir(id):
    cat = Categoria.query.get_or_404(id)
    db.session.delete(cat)
    db.session.commit()
    flash('Categoria excluída.')
    return redirect(url_for('categorias.listar'))