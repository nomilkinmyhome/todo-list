from flask import render_template

from .blueprint import blueprint


@blueprint.route('/')
def index():
    return render_template('index.html')
