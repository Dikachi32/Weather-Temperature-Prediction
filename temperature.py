from flask import Flask, render_template, request, redirect
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("temperature_predictor.pkl")

@app.route("/", methods=['GET', 'POST'])
def predict():
    prediction = None

    if request.method == "POST":

        day = request.form.get("day")
        humidity = request.form.get("humidity")
        pressure = request.form.get("pressure")
        wind_speed = request.form.get("wind_speed")
        rainfall = request.form.get("rainfall")
        sunlight = request.form.get("sunlight")

        if not day or not humidity or not pressure or not wind_speed or not rainfall or not sunlight:
            return redirect("/")

        try:
            day = float(day)
            humidity = float(humidity)
            pressure = float(pressure)
            wind_speed = float(wind_speed)
            rainfall = float(rainfall)
            sunlight = float(sunlight)
        except ValueError:
            return render_template("temperature_predictor.html", prediction="Invalid input")

        our_data = [[day, humidity, pressure, wind_speed, rainfall, sunlight]]

        prediction = model.predict(our_data)[0]
        prediction = round(prediction, 2)

    return render_template("temperature_predictor.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')