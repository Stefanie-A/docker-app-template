from flask import Flask, jsonify, request, Blueprint
from flask_migrate import Migrate
from database import db
from routes import todo_bp


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def Docker():
     return jsonify({"Dockerfile Tutorial"})

app.register_blueprint(todo_bp)
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)