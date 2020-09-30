from flask import Blueprint
from flask import request
from flask import session
from flask import render_template

#Use of blue print to group routes, 
# name - first argument is the blue print name 
# import name - second argument - helps identify the root url for it 
mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    return render_template("index.html")