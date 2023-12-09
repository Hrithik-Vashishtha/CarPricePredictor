# Kushmanda Predictions Documentation

# Overview

Kushmanda Predictions is a machine learning-based application that predicts car purchase amounts based on user input. It involves a Flask web application, a trained machine learning model, and a MySQL database for data storage.

# Features

User-friendly web interface to input data for prediction.
Machine learning model prediction for car purchase amounts.
Storage and retrieval of predicted values in a MySQL database.
Responsive interface design using HTML/CSS.

# Project Structure

The project consists of several components:

# Files

# ai_model.py: 
Python script for training the machine learning model based on the 'Car_Purchasing_Data.csv' dataset.
# app.py: 
Flask web application for handling user input, model prediction, and database operations.
# data_preprocessing.py: 
Script for data preprocessing using MinMaxScaler.
# Dockerfile: 
Configuration file for building a Docker image.
# entrypoint.sh: 
Shell script for initializing the Docker container.
# requirements.txt: 
File listing Python dependencies.

# Directories

# templates: 
Contains HTML templates for the web interface.
# static: 
Contains CSS for styling the HTML templates.

# Setup Instructions

# Requirements

Docker installed and configured
MySQL server running

# Installation Steps
1. Clone the repository:
git clone https://github.com/your-username/Kushmanda_Assignment.git
cd Kushmanda_Assignment

2. Build the Docker image:

docker build -t kushmanda_predictions .

3. Run the Docker container:

docker run -p 5000:5000 -d kushmanda_predictions

# Usage
1. Access the application by opening a web browser and navigating to http://localhost:5000.
2. Fill in the form fields (Gender, Age, Annual Salary, Credit Card Debt, Net Worth) and click 'Predict' to get the predicted purchase amount.
3. Use the 'Get Prediction' button to retrieve stored predictions based on their ID.

# Additional Notes
The application uses MinMaxScaler for data normalization during prediction.
Ensure proper MySQL configurations for database operations.
Authors
Hrithik Vashishtha
