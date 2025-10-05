from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load('spam_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')
print("--- Model and vectorizer loaded successfully ---")

@app.route('/predict', methods=['POST'])
def predict():
    """
    Receives a JSON request with a 'message' and returns a spam prediction.
    """
  
    data = request.get_json()

   
    if not data or 'message' not in data:
        return jsonify({'error': 'Missing "message" key in request body'}), 400

    message = data['message']
    
    
    message_counts = vectorizer.transform([message])
    
   
    prediction = model.predict(message_counts)
    
 
    label = 'spam' if prediction[0] == 1 else 'ham'
  
    return jsonify({
        'message': message,
        'prediction': label
    })


if __name__ == '__main__':
    
    app.run(debug=True)
