from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "your_api_key_here"  # Replace with your real API key
API_URL = "https://api.stability.ai/v1/generate"  # Modify if using other APIs

@app.route("/", methods=["GET", "POST"])
def index():
    image_url = None
    if request.method == "POST":
        prompt = request.form["prompt"]
        response = requests.post(API_URL, headers={
            "Authorization": f"Bearer {API_KEY}"
        }, json={"prompt": prompt})
        if response.status_code == 200:
            data = response.json()
            image_url = data.get("image_url")  # Make sure to match the API's JSON key
        else:
            image_url = "error"
    return render_template("index.html", image_url=image_url)

if __name__ == "__main__":
    app.run(debug=True)
