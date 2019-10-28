from flask import Flask, request
from flask import jsonify

app = Flask(__name__)
import os

domain = os.getenv('domain')


@app.route('/')
def hello_world():
    return jsonify(
        dict(domain=domain, message='home', path=request.path)
    )


@app.route('/hello-world')
def el():
    return jsonify(
        dict(domain=domain, message='hello-world', path=request.path)
    )


@app.route('/<path:path_name>')
def el_path(path_name):
    return jsonify(
        dict(domain=domain, path=request.path, message=path_name)
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0')
