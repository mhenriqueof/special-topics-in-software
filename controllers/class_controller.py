from flask import Blueprint, render_template, request, redirect, url_for, session
from controllers.utils.generators import Generator
generator = Generator()

class_bp = Blueprint('class_bp', __name__)

@class_bp.route('/class', methods=['GET', 'POST'])
def choose_class():
    if request.method == 'POST':
        session['class'] = request.form.get('class')
        return redirect(url_for('name_bp.choose_name'))
    return render_template('class.html',
                           mage=generator.generate_class('Mage'),
                           thief=generator.generate_class('Thief'),
                           warrior=generator.generate_class('Warrior'))
    