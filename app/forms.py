from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, TextAreaField, BooleanField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from app.models import Usuario, Categoria

class RegistrationForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(min=3, max=100)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=6)])
    confirmar_senha = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('senha')])
    submit = SubmitField('Registrar')
    def validate_email(self, email):
        if Usuario.query.filter_by(email=email.data).first():
            raise ValidationError('Email já registrado.')

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Entrar')

class RotinaForm(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired(), Length(max=100)])
    descricao = TextAreaField('Descrição')
    categoria_id = SelectField('Categoria', coerce=int, validators=[DataRequired()])
    ativa = BooleanField('Ativa', default=True)
    submit = SubmitField('Salvar')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.categoria_id.choices = [(c.id, c.nome) for c in Categoria.query.order_by('nome').all()]

class CategoriaForm(FlaskForm):
    nome = StringField('Nome da Categoria', validators=[DataRequired(), Length(max=64)])
    submit = SubmitField('Salvar')