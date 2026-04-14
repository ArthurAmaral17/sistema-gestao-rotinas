from flask import render_template
from flask_login import login_required
from app.main import bp

@bp.route('/')
def index():
    return render_template('index.html', title='Início')

@bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', title='Dashboard')