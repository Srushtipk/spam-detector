# spam-detector
Spam Detection REST API
Project Overview
This project is a complete, end-to-end machine learning application that classifies SMS messages as either "spam" or "ham" (not spam).

It consists of two main parts:

A training script (train_model.py) that takes a raw dataset of labeled SMS messages, processes the text, and trains a Naive Bayes classifier. The script then saves the trained model and the text vectorizer to disk.

A Flask API (app.py) that loads the saved model and exposes a /predict endpoint. This allows other applications to send new, unseen messages to the API and receive a real-time prediction in JSON format.

Technologies Used
Language: Python

Machine Learning: Scikit-learn

Data Manipulation: Pandas

Web Framework: Flask

Model Serialization: Joblib

Setup and Usage
Follow these steps to set up the environment and run the API on your local machine.

1. Create a Virtual Environment
First, create and activate a virtual environment to keep the project dependencies isolated.

# Create the virtual environment
py -m venv venv

# Activate the environment (for Windows PowerShell)
.\venv\Scripts\activate

2. Install Dependencies
Install all the required libraries from the requirements.txt file.

pip install -r requirements.txt

3. Download the Dataset
The model training script requires the SMS Spam Collection Dataset from Kaggle.

Download the dataset from the link above.

Unzip the file.

Place the spam.csv file in the root of the project directory.

4. Train the Model
Run the training script. This will process the data and create two files: spam_model.pkl and vectorizer.pkl.

py train_model.py

5. Run the API
Once the model is trained, you can start the Flask server.

py app.py

The API will now be running at http://127.0.0.1:5000.

6. Test the API
You can send a POST request to the /predict endpoint to get a prediction. Here is an example using curl in PowerShell:

# Example of a spam message
curl -Uri [http://127.0.0.1:5000/predict](http://127.0.0.1:5000/predict) -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"message": "free viagra click here now"}'

# Example of a ham message
curl -Uri [http://127.0.0.1:5000/predict](http://127.0.0.1:5000/predict) -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"message": "Hey, are you free for dinner tonight?"}'
