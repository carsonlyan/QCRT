from flask import Blueprint


author = Blueprint('author', __name__)


from . import login