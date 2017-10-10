# _*_coding_*_ utf-8
# Author Abin
# Date = '2017/9/24 19:56'

from flask import Blueprint

home = Blueprint('home', __name__)

from app.home import views
