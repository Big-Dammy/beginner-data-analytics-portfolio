# Import file tools, pandas, charts, and machine-learning evaluation tools.
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (classification_report, confusion_matrix,
                             ConfusionMatrixDisplay, average_precision_score)

# Set up paths based on this script's location.
HERE = Path(__file__).resolve().parent
DATA_FILE = HERE / "data" / "transactions_demo.csv"
OUTPUT_FOLDER = HERE / "outputs"
OUTPUT_FOLDER.mkdir(exist_ok=True)

# Read the generated transaction data.
data = pd.read_csv(DATA_FILE)

# Select the columns the model can use as clues.
feature_columns = ["amount", "hour", "merchant_risk_score", "distance_from_home_km", "card_present"]
features = data[feature_columns]
labels = data["is_fraud"]

# Split the rows while keeping a similar fraud percentage in each part.
X_train, X_test, y_train, y_test = train_test_split(
    features, labels, test_size=0.25, random_state=42, stratify=labels
)

# Train a modest Random Forest. Class weighting helps pay attention to the rare class.
model = RandomForestClassifier(
    n_estimators=100, random_state=42, class_weight="balanced_subsample", n_jobs=-1
)
model.fit(X_train, y_train)

# Predict labels and probabilities for the held-back test rows.
predictions = model.predict(X_test)
probabilities = model.predict_proba(X_test)[:, 1]

# Report more than accuracy because fraud cases are uncommon in this demo.
report = classification_report(y_test, predictions, zero_division=0)
average_precision = average_precision_score(y_test, probabilities)
summary = "SYNTHETIC DEMO ONLY\n" + report + f"\nAverage precision: {average_precision:.3f}\n"
print(summary)
(OUTPUT_FOLDER / "model_report.txt").write_text(summary, encoding="utf-8")

# Draw a confusion matrix to compare true labels with model predictions.
ConfusionMatrixDisplay(confusion_matrix(y_test, predictions), display_labels=["Not fraud", "Fraud"]).plot()
plt.title("Fraud Demo - Confusion Matrix")
plt.tight_layout()
plt.savefig(OUTPUT_FOLDER / "confusion_matrix.png")
plt.close()

# Save a small, inspectable set of predictions without any real personal information.
preview = X_test.reset_index(drop=True).copy()
preview["actual_label"] = y_test.reset_index(drop=True)
preview["predicted_label"] = predictions
preview["predicted_fraud_probability"] = probabilities.round(3)
preview.head(200).to_csv(OUTPUT_FOLDER / "prediction_sample.csv", index=False)
print("Finished. Scores are not evidence of real-world fraud detection performance.")
