from flask import Flask, request, jsonify, render_template , redirect
import os
import pickle

app = Flask(__name__)
port = int(os.getenv('PORT', '3000'))


@app.route('/', methods=['GET','POST'])
def home():
    return render_template('index.html')

# make prediction 
@app.route('/predict', methods=['POST','GET'])
def predict():
    return "yo les noob"




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)