# Corrige todos os arquivos de uma vez
Set-Content -Path app\templates\index.html -Encoding UTF8 -Value @"
{% extends "base.html" %}
{% block content %}
<div class="p-5 bg-light rounded-3">
  <h1 class="display-4">Gestão de Rotinas</h1>
  <p class="lead">Organize seu dia a dia.</p>
  {% if not current_user.is_authenticated %}
  <a href="{{ url_for('auth.register') }}" class="btn btn-primary btn-lg">Começar</a>
  <a href="{{ url_for('auth.login') }}" class="btn btn-outline-secondary btn-lg">Login</a>
  {% else %}
  <a href="{{ url_for('rotinas.listar') }}" class="btn btn-success btn-lg">Minhas Rotinas</a>
  {% endif %}
</div>
{% endblock %}
"@

Set-Content -Path app\templates\categorias\listar.html -Encoding UTF8 -Value @"
{% extends "base.html" %}
{% block content %}
<div class="d-flex justify-content-between mb-3">
  <h2>Categorias</h2>
  <a href="{{ url_for('categorias.criar') }}" class="btn btn-primary">Nova</a>
</div>
<table class="table">
  <thead><tr><th>Nome</th><th>Ações</th></tr></thead>
  <tbody>
    {% for c in categorias %}
    <tr><td>{{ c.nome }}</td><td><a href="{{ url_for('categorias.excluir', id=c.id) }}" class="btn btn-sm btn-outline-danger" onclick="return confirm('Excluir?')">Excluir</a></td></tr>
    {% endfor %}
  </tbody>
</table>
{% endblock %}
"@

Set-Content -Path app\templates\categorias\criar.html -Encoding UTF8 -Value @"
{% extends "base.html" %}
{% block content %}
<div class="row justify-content-center">
  <div class="col-md-6">
    <div class="card shadow">
      <div class="card-header bg-primary text-white">Nova Categoria</div>
      <div class="card-body">
        <form method="POST">
          {{ form.hidden_tag() }}
          <div class="mb-3">{{ form.nome.label }} {{ form.nome(class="form-control") }}</div>
          {{ form.submit(class="btn btn-primary") }}
          <a href="{{ url_for('categorias.listar') }}" class="btn btn-secondary">Cancelar</a>
        </form>
      </div>
    </div>
  </div>
</div>
{% endblock %}
"@

Set-Content -Path app\categorias\routes.py -Encoding UTF8 -Value @"
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
"@

Write-Host "ARQUIVOS CORRIGIDOS COM SUCESSO!" -ForegroundColor Green