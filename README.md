# 🔒 Hybrid Phishing URL Detector

A web-based phishing URL detection system that combines **Machine Learning** and **Rule-Based Analysis** to identify malicious websites. The application is built using **Python** and **Flask**, providing users with a simple interface to check whether a URL is **Safe**, **Suspicious**, or **Phishing**.

---

## 📌 Project Overview

Phishing attacks trick users into revealing sensitive information through fake websites. This project detects phishing URLs by combining:

- Rule-based URL analysis
- Machine Learning prediction
- Flask web application

The hybrid approach improves detection by using both predefined security rules and a trained ML model.

---

## ✨ Features

- 🔍 Detects phishing URLs
- 🤖 Machine Learning-based prediction
- 📋 Rule-based URL analysis
- 🌐 Flask web interface
- ⚡ Fast prediction results
- 💻 Easy to run locally

---

## 🛠️ Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- Joblib
- HTML
- CSS

---

## 📁 Project Structure

```
hybrid-phishing-url-detector/
│
├── app.py
├── detector.py
├── train_model.py
├── train_phishing_model.py
├── model.pkl
├── vectorizer.pkl
├── scaler.pkl
├── templates/
│   ├── index.html
│   └── warning.html
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/srivaishnavi1311-rgb/hybrid-phishing-url-detector.git
```

Install the required packages:

```bash
pip install flask pandas numpy scikit-learn joblib
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 🧠 How It Works

1. User enters a URL.
2. The system performs rule-based checks.
3. The trained Machine Learning model analyzes the URL.
4. Both results are combined.
5. The application classifies the URL as:

- ✅ Safe
- ❌ Phishing

---

## 🚀 Future Enhancements

- Browser Extension
- Real-time URL Reputation API
- Deep Learning Model
- Dark Mode UI
- Cloud Deployment

---

## 👩‍💻 Author

**Sri Vaishnavi V and Sandhiya V**

B.Tech – Artificial Intelligence & Data Science

Kings Engineering College

GitHub: https://github.com/srivaishnavi1311-rgb

---
## 📸 Screenshots

### 🏠 Home Page

<img width="1918" height="968" alt="Home" src="https://github.com/user-attachments/assets/8febe1cb-11c7-41c1-96cc-6bacc3779178" />


---

### ✅ Safe URL Detection


<img width="1918" height="968" alt="Safe" src="https://github.com/user-attachments/assets/5f6ce01a-4d4a-428c-885c-0a59ac1d19cd" />


---

### ❌ Phishing URL Detection


<img width="1918" height="965" alt="Suspicious" src="https://github.com/user-attachments/assets/49c12f03-9838-479a-8b18-ada21e93f9d5" />


---
