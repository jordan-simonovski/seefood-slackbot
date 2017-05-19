from flask import Flask, jsonify, json, request
from modules import *
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def lambda_handler(event=None, context=None):
    if request.method == 'POST':
        answerMessage = rekognition.rekImage(request.form)
        return jsonify(answerMessage)
