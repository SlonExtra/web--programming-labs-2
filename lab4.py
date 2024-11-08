from flask import Blueprint, render_template, request

bp = Blueprint('lab4', __name__)

@bp.route('/lab4')
def lab4():
    return render_template('lab4/lab4.html')