from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load Model
with open("loan_model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    age = float(request.form["age"])
    income = float(request.form["income"])
    loan_amount = float(request.form["loan_amount"])
    credit_score = float(request.form["credit_score"])

    data = np.array(
        [[age, income, loan_amount, credit_score]]
    )

    prediction = model.predict(data)

    if prediction[0] == 1:
        result = "✅ Loan Approved"
    else:
        result = "❌ Loan Rejected"

    return render_template(
        "index.html",
        prediction_text=result
    )

if __name__ == "__main__":
    app.run(debug=True)