from flask import Blueprint, render_template, session
from controllers.utils.generators import Generator
generator = Generator()

character_bp = Blueprint('character_bp', __name__)

@character_bp.route('/character')
def character():
    attributes = session.get('attributes', {})
    race = session.get('race', '')
    klass = session.get('class', '')
    name = session.get('name', '')
    character = generator.generate_character(name, attributes, race, klass)
    return render_template('character.html', character=character)
