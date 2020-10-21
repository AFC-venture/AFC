from flask import Blueprint


admin_app = Blueprint('admin', __name__, url_prefix="/admin",  template_folder='templates')