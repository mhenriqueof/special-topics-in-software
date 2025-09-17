from flask import Blueprint, render_template, request, redirect, url_for, session
from controllers.utils.generators import Generator
generator = Generator()

race_bp = Blueprint('race_bp', __name__)

@race_bp.route('/race', methods=['GET', 'POST'])
def choose_race():
    if request.method == 'POST':
        session['race'] = request.form.get('race')
        return redirect(url_for('class_bp.choose_class'))
    return render_template('race.html',
                           elf=generator.generate_race('Elf'),
                           halfling=generator.generate_race('Halfling'),
                           human=generator.generate_race('Human'))
    