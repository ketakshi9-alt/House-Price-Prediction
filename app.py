from flask import Flask, render_template, request
import pickle
import pandas as pd


app = Flask(__name__)

# Load trained model
model = pickle.load(open("Model/model_linear.pkl", "rb"))

def format_inr_indian_style(n):
    """Format number like 6578990 → '65,78,990'"""
    s = str(int(n))
    if len(s) <= 3:
        return s
    # Last 3 digits
    result = s[-3:]
    s = s[:-3]
    # Then every 2 digits (lakhs, crores, etc.)
    while s:
        result = s[-2:] + ',' + result
        s = s[:-2]
    return result

@app.template_filter("inr")
def inr_filter(n):
    if n is None:
        return ""
    return format_inr_indian_style(n)

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        area = float(request.form["area"])
        bedrooms = int(request.form["bedrooms"])
        bathrooms = int(request.form["bathrooms"])
        stories = int(request.form["stories"])
        mainroad = int(request.form["mainroad"])
        guestroom = int(request.form["guestroom"])
        basement = int(request.form["basement"])
        hotwaterheating = int(request.form["hotwaterheating"])
        airconditioning = int(request.form["airconditioning"])
        parking = int(request.form["parking"])
        prefarea = int(request.form["prefarea"])
        furnishingstatus = int(request.form["furnishingstatus"])

        data = pd.DataFrame(
            [[
                area, bedrooms, bathrooms, stories,
                mainroad, guestroom, basement,
                hotwaterheating, airconditioning,
                parking, prefarea, furnishingstatus
            ]],
            columns=[
                'area', 'bedrooms', 'bathrooms', 'stories',
                'mainroad', 'guestroom', 'basement',
                'hotwaterheating', 'airconditioning',
                'parking', 'prefarea', 'furnishingstatus'
            ]
        )

        pred_value = model.predict(data)[0]
        prediction = round(pred_value, 2)

    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)