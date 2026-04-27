# 🌤️ Weather Temperature Prediction System

## 📌 Overview

This project is a Machine Learning web application that predicts temperature based on environmental conditions such as day, humidity, pressure, wind speed, rainfall, and sunlight.

Users can input weather data through a simple web interface, and the model will instantly predict the temperature.


## 🚀 Features

* Predict temperature (°C) using:

  * Day
  * Humidity (%)
  * Pressure (hPa)
  * Wind Speed (km/h)
  * Rainfall (mm)
  * Sunlight (hours)
* Real-time predictions
* Clean and interactive web interface
* Lightweight and fast model


## 🧠 Machine Learning

* Algorithm: Linear Regression
* Library: Scikit-learn
* Evaluation Metrics:

  * Mean Squared Error (MSE)
  * R² Score

---

## 🛠️ Tech Stack

* Python
* Flask
* NumPy
* Pandas
* Scikit-learn
* Joblib


## 📂 Project Structure

```
weather-temperature-prediction/
│
├── temperature.py
├── temperature_predictor.pkl
├── weather_500.csv
├── requirements.txt
│
├── templates/
│   └── temperature_predictor.html
│
└── notebook/
    └── temperature_pred.ipynb
```


## ▶️ How to Run Locally

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Run the Flask app:

```
python temperature.py
```

3. Open your browser:

```
http://127.0.0.1:5000
```


## ⚠️ Notes

* Ensure all input values are numeric
* Model predictions depend on the quality of training data
* Input features must match training features

---

## 💡 Future Improvements

* Improve UI/UX design
* Add more advanced ML models
* Deploy the application online
* Add better input validation and error handling


## 👨‍💻 Author

Francis Onyedikachi (Dikachi)
