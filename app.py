from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests

# Creating the Flask application
app = Flask(__name__)
CORS(app)

# Defining the routes
@app.route('/')  # Home route serving index.html
def home():
    return render_template("index.html")

# Handling translation requests
@app.route("/translate", methods=["POST"])
def translate():
    data = request.json
    source_text = data.get("text")
    source_lang = data.get("sourceLang")
    target_lang = data.get("targetLang")
    api_key = "b0b833a760msh21eacf2806b7995p19e44bjsnb8e5c8a30d0c"

    url = "https://microsoft-translator-text.p.rapidapi.com/translate?api-version=3.0"
    headers = {
        'content-type': 'application/json',
        'x-rapidapi-host': 'microsoft-translator-text.p.rapidapi.com',
        'x-rapidapi-key': api_key
    }

    # Constructing payload as required by Microsoft Translator API
    payload = [{
        "Text": source_text
    }]
    params = {
        "from": source_lang,  # Specify the source language
        "to": target_lang     # Specify the target language
    }

    # Make the API request
    response = requests.post(url, headers=headers, params=params, json=payload)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Translation API error"}), response.status_code

# Run the Flask app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
