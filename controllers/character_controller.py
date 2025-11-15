import json
import os
import tempfile
from flask import Blueprint, render_template, session, redirect, url_for, flash, send_file
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
    character_dict = {
        'name': character.name,
        'attributes': character.attributes,
        'race': character.race.__dict__, 
        'klass': character.klass.__dict__
    }    
    session['character_dict'] = character_dict
    return render_template('character.html', character=character)

@character_bp.route('/character/save_character', methods=['POST'])
def save_character():
    data_to_save = session.get('character_dict', {})

    try:
        temp_file_path = os.path.join(tempfile.gettempdir(), f"character.json")
        with open(temp_file_path, 'w', encoding='utf-8') as f:
            json.dump(data_to_save, f, ensure_ascii=False, indent=4)
        response = send_file(
            temp_file_path,
            as_attachment=True,
            download_name=f"character.json",
            mimetype='application/json'
        )
        return response
    
    except Exception as e:
        flash(f'Error: {e}', 'error')
        return redirect(url_for('character_bp.character'))
    