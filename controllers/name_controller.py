from flask import Blueprint, render_template, request, redirect, url_for, session

name_bp = Blueprint('name_bp', __name__)

@name_bp.route('/name', methods=['GET', 'POST'])
def choose_name():
    if request.method == 'POST':
        session['name'] = request.form.get('name')
        return redirect(url_for('character_bp.character'))
    return render_template('name.html')
