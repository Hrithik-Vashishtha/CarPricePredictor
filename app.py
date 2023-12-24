#Gender	Age	Annual Salary	Credit Card Debt	Net Worth
from flask import Flask, request, jsonify, render_template
import numpy as np
from data_preprocessing import DataPreprocessing
from tensorflow.keras.models import load_model
import mysql.connector

print("Hello")

app = Flask(__name__)

#change the path of model accordingly to run it on local or on cloud
model = load_model('C:/Users/Hrithik/Desktop/Kushmanda_Assignment/trained_model.keras')

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="hrithik",
    database="predictions"
)   

mycursor = mydb.cursor()

# create dabatbase = CREATE DATABASE predictions;
# Create Table = CREATE TABLE predicted_data (id INT AUTO_INCREMENT PRIMARY KEY, Gender INT, Age INT, Salary FLOAT, Debt FLOAT, Net_Worth FLOAT, Purchase_Amount FLOAT);
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

    return jsonify(f'Predicted Purchase Amount for the user: {output}'), 200

@app.route('/get_predictions/<int:id>', methods = ['GET'])
def get_predictions(id):
    if id:
        query = 'select * from predicted_data where id = %s'
        mycursor.execute(query, (id,))
        result = mycursor.fetchall()
        if result:
            return jsonify({'Purchase Amount':result[0][6]}), 200
        return jsonify("id not found"), 400
    return jsonify("id not provided"), 400

    
@app.route('/get_all_predictions', methods=['GET'])
def get_all_predictions():
    query = 'SELECT * FROM predicted_data'
    mycursor.execute(query)
    result = mycursor.fetchall()

    if result:
        predictions = []
        for row in result:
            prediction = {
                'ID': row[0],
                'Gender': row[1],
                'Age': row[2],
                'Salary': row[3],
                'Debt': row[4],
                'Net Worth': row[5],
                'Purchase Amount': row[6]
            }
            predictions.append(prediction)
        return jsonify(predictions)
    return jsonify("No predictions found")

if __name__ == '__main__':
    app.run(debug=True)
