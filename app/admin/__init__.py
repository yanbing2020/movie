# _*_coding_*_ utf-8
# Author Abin
# Date = '2017/9/24 19:56'

from flask import Blueprint

admin = Blueprint('admin', __name__)

from app.admin import views
