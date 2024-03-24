from flask import Flask, jsonify, Blueprint
from flask_migrate import Migrate
from database import * 

app = Flask(__name__)
todo_bp =Blueprint('task', '__name__')

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/home')
def docker():
     return jsonify("Dockerfile Tutorial")

app.register_blueprint(todo_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)