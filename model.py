import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

# Load Dataset
df = pd.read_csv("loan_data.csv")

# Features
X = df[["Age", "Income", "LoanAmount", "CreditScore"]]

# Target
y = df["Approved"]

# Train Model
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

# Save Model
with open("loan_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model Trained Successfully!")