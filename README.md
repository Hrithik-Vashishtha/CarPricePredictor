# Kushmanda Predictions Documentation

## Overview

Kushmanda Predictions is a machine learning-based application that predicts car purchase amounts based on user input. It involves a Flask web application, a trained machine learning model, and a MySQL database for data storage.

## Features

- User-friendly web interface to input data for prediction.
- Machine learning model prediction for car purchase amounts.
- Storage and retrieval of predicted values in a MySQL database.
- Responsive interface design using HTML/CSS.

## Project Structure

The project consists of several components:

### Files

- **ai_model.py**: Python script for training the machine learning model based on the 'Car_Purchasing_Data.csv' dataset.
- **app.py**: Flask web application for handling user input, model prediction, and database operations.
- **data_preprocessing.py**: Script for data preprocessing using MinMaxScaler.
- **Dockerfile**: Configuration file for building a Docker image.
- **entrypoint.sh**: Shell script for initializing the Docker container.
- **requirements.txt**: File listing Python dependencies.
- **services.yaml**: Kubernetes Service configuration for the application.
- **deployment.yaml**: Kubernetes Deployment configuration for the application.

### Directories

- **templates**: Contains HTML templates for the web interface.
- **static**: Contains CSS for styling the HTML templates.

## Setup Instructions

### Requirements

- Docker installed and configured
- MySQL server running

### Installation Steps

# Installation Steps
1. Clone the repository:
git clone https://github.com/Hrithik-Vashishtha/Kushmanda_Assignment.git
cd Kushmanda_Assignment



2. First run ai_model.py to create a model and then adjust its path in app.py line 11       accordingly.

3. Create a "predictions" database by running the command "create database predictions;"
   
4. Create table "predicted_data" by running the command "mycursor.execute("CREATE TABLE       predicted_data (id INT AUTO_INCREMENT PRIMARY 
   KEY, Gender INT, Age INT, Salary FLOAT, Debt FLOAT, Net_Worth FLOAT, Purchase_Amount FLOAT)")

4. Build the Docker image:
   docker build -t kushmanda:v1 .

5. Run the Docker container:
   docker run -p 3306:3306 -p 5000:5000 kushmanda:v1

6. Apply Kubernetes Deployment configuration:
   kubectl apply -f deployment.yaml

7. Apply Kubernetes Service configuration:
   kubectl apply -f service.yaml


### Usage

1. Access the application by opening a web browser and navigating to http://localhost:5000.
2. Fill in the form fields (Gender, Age, Annual Salary, Credit Card Debt, Net Worth) and click 'Predict' to get the predicted purchase amount.
3. Use the '/get_predictions/<int:id>' API to retrieve stored predictions based on their ID.
4. Use the '/get_all_predictions' API to retrieve all predictions.

### Additional Notes

- The application uses MinMaxScaler for data normalization during prediction.
- Ensure proper MySQL configurations for database operations.

## Authors

Hrithik Vashishtha

