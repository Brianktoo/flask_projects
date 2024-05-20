from flask import Blueprint
addition_bp = Blueprint('addition_bp', __name__)
from . import routes

# def  create_app(app):
#     app = Flask(__name__)

#     with app.app_context():
#         from. import routes
#     return app    

