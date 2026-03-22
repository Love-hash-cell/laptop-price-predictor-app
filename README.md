# 💻 Laptop Price Prediction Web App

## 🚀 Overview
This project is a Machine Learning-based web application that predicts laptop prices based on user inputs such as RAM, weight, and touchscreen availability.

The application integrates a trained ML model with a Flask backend and a simple frontend interface, allowing real-time predictions.

---

## 📸 Screenshots

### 🏠 Initial UI (Before Input)
This is the interface where users can enter laptop specifications:

![Initial UI](homepage.png)

---

### 💰 Prediction Result (After Input)
After entering values, the model predicts the laptop price instantly:

![Prediction Result](result.png)

---

## 🧠 Tech Stack

- Machine Learning: Scikit-learn (Random Forest)
- Backend: Flask
- Frontend: HTML, CSS, JavaScript
- Deployment: Render
- Language: Python

---

## ⚙️ Features

- 🔍 Predict laptop price instantly
- 🧠 Machine Learning model (Random Forest)
- ⚡ Fast API using Flask
- 💻 Clean and user-friendly interface
- 🔗 REST API integration
- 🌐 Ready for deployment

---

## 🧪 How It Works

1. User enters laptop specifications (RAM, Weight, Touchscreen)
2. Frontend sends data to Flask API
3. Backend processes input using trained ML model
4. Model predicts laptop price
5. Result is displayed instantly on the UI

---

## 📁 Project Structure

│
├── app.py
├── model.pkl
├── columns.pkl
├── requirements.txt
├── Procfile
├── index.html
├── README.md
│
└── screenshots/
├── home.png
└── result.png
