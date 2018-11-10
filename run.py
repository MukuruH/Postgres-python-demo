from flask import Flask, jsonify, request

from models import Product

app = Flask(__name__)

products = []


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
	app.run(debug=True)