from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date
from app import db, login_manager

class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha_hash = db.Column(db.String(128))
    rotinas = db.relationship('Rotina', backref='usuario', lazy='dynamic')
    execucoes = db.relationship('ExecucaoDiaria', backref='usuario', lazy='dynamic')

    def set_senha(self, senha):
        self.senha_hash = generate_password_hash(senha)
    def check_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

class Categoria(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), unique=True, nullable=False)
    rotinas = db.relationship('Rotina', backref='categoria', lazy='dynamic')

class Rotina(db.Model):
    __tablename__ = 'rotinas'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text)
    ativa = db.Column(db.Boolean, default=True, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    execucoes = db.relationship('ExecucaoDiaria', backref='rotina', lazy='dynamic', cascade='all, delete-orphan')
class ExecucaoDiaria(db.Model):
    __tablename__ = 'execucoes_diarias'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False, default=date.today)
    concluida = db.Column(db.Boolean, default=True)
    rotina_id = db.Column(db.Integer, db.ForeignKey('rotinas.id'), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)