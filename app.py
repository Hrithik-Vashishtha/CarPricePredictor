#Gender	Age	Annual Salary	Credit Card Debt	Net Worth
from flask import Flask, request, jsonify, render_template
import numpy as np
from data_preprocessing import DataPreprocessing
from tensorflow.keras.models import load_model


app = Flask(__name__)

model = load_model('C:/Users/Hrithik/Desktop/Kushmanda_Assignment/trained_model.keras')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    gender = int(request.form['gender'])
    age = int(request.form['age'])
    salary = float(request.form['salary'])
    debt = float(request.form['debt'])
    net_worth = float(request.form['net_worth'])

    user_input = np.array([[gender, age, salary, debt, net_worth]])

    data_processor = DataPreprocessing()
    processed_data = data_processor.user_data(user_input)

    output = model.predict(processed_data)
    return jsonify(f'Predicted Purchase Amount for the user: {output}')

if __name__ == '__main__':
    app.run(debug=True)
