from flask import Flask
from routes import game

app = Flask(__name__)

app.register_blueprint(game)

if __name__ == '__main__':
    app.run(debug=True)

