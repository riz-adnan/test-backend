import firebase_admin
from firebase_admin import credentials, db
from flask import Flask, request
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

cred = credentials.Certificate("./newproj-4c059-firebase-adminsdk-baj41-46bdad62c8.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://newproj-4c059-default-rtdb.asia-southeast1.firebasedatabase.app'
})

app = Flask(__name__)
CORS(app)  
@app.route('/submit-form', methods=['POST'])
def submit_form():
    form_data = request.json
    print('Form Data:', form_data)
    try:
        ref = db.reference('formSubmissions')
        ref.push(form_data)
        return 'Form data saved to Firebase successfully', 200
    except Exception as e:
        print('Error saving form data to Firebase:', e)
        return 'Internal Server Error', 500

if __name__ == '__main__':
    app.run(debug=True)
