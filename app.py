from flask import Flask, request, render_template
import pickle
from scipy.sparse import hstack
import socket

app = Flask(__name__)

# ------------------------------
# Load model, vectorizer, and scaler
# ------------------------------
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# ------------------------------
# Feature extraction function
# ------------------------------
def extract_numeric_features(url):
    url = url.lower()
    url_len = len(url)
    num_dots = url.count('.')
    num_hyphens = url.count('-')
    has_https = 1 if url.startswith("https://") else 0
    num_digits = sum(c.isdigit() for c in url)
    return [[url_len, num_dots, num_hyphens, has_https, num_digits]]

# ------------------------------
# Whitelist for critical URLs
# ------------------------------
whitelist = [
    "https://www.icicibank.com",
    "https://www.sbi.co.in",
    "https://www.hdfcbank.com",
    "https://www.axisbank.com",
    "https://www.india.gov.in",
    "https://www.mca.gov.in",
]

# ------------------------------
# Helper: check if domain exists
# ------------------------------
def domain_exists(url):
    try:
        domain = url.split("//")[-1].split("/")[0].split(":")[0]
        socket.gethostbyname(domain)
        return True
    except Exception:
        return False

# ------------------------------
# Flask routes
# ------------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"].strip()

        # 1️⃣ Whitelist check
        if url in whitelist:
            result = "Safe ✅"
            alert_type = "success"
        # 2️⃣ Domain existence check
        elif not domain_exists(url):
            result = "⚠️ Warning: This site may be phishing!"
            alert_type = "danger"
        # 3️⃣ ML prediction
        else:
            numeric_features = extract_numeric_features(url)
            numeric_scaled = scaler.transform(numeric_features)
            text_features = vectorizer.transform([url])
            features_combined = hstack([text_features, numeric_scaled])
            prediction = model.predict(features_combined)[0]
            if prediction == 1:
                result = "⚠️ Warning: This site may be phishing!"
                alert_type = "danger"
            else:
                result = "Safe ✅"
                alert_type = "success"

        return render_template("index.html", url=url, result=result, alert_type=alert_type)

    return render_template("index.html", url=None, result=None, alert_type=None)

# ------------------------------
# Run app
# ------------------------------
if __name__ == "__main__":
    app.run(debug=True)
