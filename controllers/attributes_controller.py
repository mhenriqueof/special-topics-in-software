from flask import Blueprint, render_template, request, session, redirect, url_for, session
from controllers.utils.generators import Generator

attributes_bp = Blueprint('attributes_bp', __name__)

@attributes_bp.route('/choose_distribution_style', methods=['GET', 'POST'])
def choose_distribution_style():
    if request.method == 'POST':
        session.clear()
        session['attribute_names'] = ['CHA (Charisma)', 'CON (Constitution)', 'DEX (Dexterity)',
                                      'INT (Intelligence)', 'STR (Strength)', 'WIS (Wisdom)']
        style = request.form.get('style', '')
        session['style'] = style
        return redirect(url_for('attributes_bp.attribute_distribution'))
    return render_template('attributes.html')

@attributes_bp.route('/attribute_distribution', methods=['GET', 'POST'])
def attribute_distribution():
    attribute_names = session.get('attribute_names', [])
    all_rolls = session.get('all_rolls', {})
    all_total = session.get('all_total', {})
    rolls = session.get('rolls', [])
    total = session.get('total', int)
    style = session.get('style', '')
    html_file = 'classic_style.html'
    if style == 'Adventure' or style == 'Heroic':
        html_file = 'adventure_heroic_style.html'
    return render_template(f'attribute_distribution/{html_file}',
                           attribute_names=attribute_names, all_rolls=all_rolls, all_total=all_total,
                           rolls=rolls, total=total, style=style)
    
@attributes_bp.route('/attribute_distribution/roll_dice', methods=['POST'])
def roll_dice():
    style = session.get('style', '')
    rolls = Generator.generate_dice_rolls(style)
    session['rolls'] = rolls
    session['total'] = sum(rolls)
    return redirect(url_for('attributes_bp.attribute_distribution'))

@attributes_bp.route('/attribute_distribution/assign_attribute', methods=['POST'])
def assign_attribute():
    style = session.get('style', '')
    rolls = session.get('rolls', [])
    total = session.get('total', int)
    if style == 'Heroic':
        rolls.remove(min(rolls))
        total = sum(rolls)
    elif style == 'Classic': # i couldn't do: button -> roll_dice() -> assign_attribute(), because of "Method Not Allowed" error
        rolls = Generator.generate_dice_rolls(style)
        total = sum(rolls)

    attribute = request.form.get('attribute', '')
    all_rolls = session.get('all_rolls', {})
    all_total = session.get('all_total', {})
    all_rolls[attribute] = rolls
    all_total[attribute] = total

    session['all_rolls'] = all_rolls
    session['all_total'] = all_total
    session['rolls'] = None # reset for next roll dice
    session['total'] = None # reset for next roll dice
    return redirect(url_for('attributes_bp.attribute_distribution'))
    
@attributes_bp.route('/create_attributes', methods=['POST'])
def create_character_attributes():
    attribute_names = session.get('attribute_names', [])
    all_total = session.get('all_total', {})
    
    attributes = {}
    for attribute in attribute_names:
        attributes[attribute] = all_total[attribute]
    
    session['attributes'] = attributes
    return redirect(url_for('race_bp.choose_race'))
