from flask import Flask, request, jsonify, Blueprint
from routes import task_bp
from flask_migrate import Migrate
from database import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/database_name'
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def docker():
     return "Dockerfile Tutorial"

app.register_blueprint(task_bp)
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)