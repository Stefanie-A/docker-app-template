from flask import Flask, request, jsonify, Blueprint
from flask_migrate import Migrate
from database import * 

app = Flask(__name__)
task_bp =Blueprint('task', '__name__')

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def docker():
     return jsonify("Dockerfile Tutorial")

app.register_blueprint(task_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)