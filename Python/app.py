from flask import Flask, request, jsonify, Blueprint

app = Flask(__name__)

@app.route('/')
def docker():
     return "Dockerfile Tutorial"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)