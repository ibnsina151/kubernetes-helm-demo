from flask import Flask
from flask import jsonify
app = Flask(__name__)
import os
domain = os.getenv('domain')
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hello-world')
def el():
    return jsonify(
        dict(domain=domain,message='hello-world')
    )




if __name__ == '__main__':
    app.run(host='0.0.0.0')
