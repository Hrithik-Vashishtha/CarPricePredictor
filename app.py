#Gender	Age	Annual Salary	Credit Card Debt	Net Worth
from flask import Flask, request, jsonify, render_template
import numpy as np
from data_preprocessing import DataPreprocessing
from tensorflow.keras.models import load_model
import mysql.connector

app = Flask(__name__)

model = load_model('C:/Users/Hrithik/Desktop/Kushmanda_Assignment/trained_model.keras')

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="09041997",
    database="predictions"
)   

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE predicted_data (id INT AUTO_INCREMENT PRIMARY KEY, Gender INT, Age INT, Salary FLOAT, Debt FLOAT, Net_Worth FLOAT, Purchase_Amount FLOAT)")
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

    output = float(output[0][0])

    query = "INSERT INTO predicted_data (Gender, Age, Salary, Debt, Net_Worth, Purchase_Amount) values (%s, %s, %s, %s, %s, %s)"
    values = (gender, age, salary, debt, net_worth, output)
    mycursor.execute(query, values)
    mydb.commit()

    return jsonify(f'Predicted Purchase Amount for the user: {output}')

@app.route('/get_predictions/<int:id>', methods = ['GET'])
def get_predictions(id):
    if id:
        query = 'select * from predicted_data where id = %s'
        mycursor.execute(query, (id,))
        result = mycursor.fetchall()
        if result:
            return jsonify({'Purchase Amount':result[0][6]})
        return jsonify("id not found")
    return jsonify("id not provided")

if __name__ == '__main__':
    app.run(debug=True)
