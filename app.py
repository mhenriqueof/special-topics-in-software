from flask import Flask
from controllers.index_controller import index_bp
from controllers.attributes_controller import attributes_bp
from controllers.race_controller import race_bp
from controllers.class_controller import class_bp
from controllers.name_controller import name_bp
from controllers.character_controller import character_bp

app = Flask(__name__)
app.secret_key = 'secret'

app.register_blueprint(index_bp)
app.register_blueprint(attributes_bp)
app.register_blueprint(race_bp)
app.register_blueprint(class_bp)
app.register_blueprint(name_bp)
app.register_blueprint(character_bp)

if __name__ == '__main__':
    app.run(debug=True)
