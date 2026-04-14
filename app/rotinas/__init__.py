from flask import Blueprint
bp = Blueprint('rotinas', __name__)
from app.rotinas import routes