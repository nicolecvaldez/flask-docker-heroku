

# import packages
from flask import Flask, jsonify, request
from model import iris_predict
import os

# paths
MODEL_PATH = "irisclassifier_knn.pkl"

app = Flask(__name__)


@app.route('/iris-classifier', methods=['POST'])
def check_fraud():

    q = request.json

    q_list = [[
        q["sepal_length"],
        q["sepal_width"],
        q["petal_length"],
        q["petal_width"]
    ]]

    prediction = iris_predict(MODEL_PATH, q_list)

    return jsonify(
        data={
            "specie": prediction})

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
