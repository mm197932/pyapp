from flask import Blueprint, render_template, request, redirect

content = Blueprint("myapp", __name__, url_prefix='/content')

@content.route('/')
def index():
    return render_template('content/index.html')