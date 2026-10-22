# Import the libraries needed for tables, charts, and a basic classification model.
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, ConfusionMatrixDisplay

# Locate the data file and create a folder for saved results.
HERE = Path(__file__).resolve().parent
DATA_FILE = HERE / "data" / "machine_sensor_data.csv"
OUTPUT_FOLDER = HERE / "outputs"
OUTPUT_FOLDER.mkdir(exist_ok=True)

# Load the synthetic sensor data.
data = pd.read_csv(DATA_FILE)

# Print average sensor readings for each machine to practise grouping data.
summary = data.groupby("machine_id", as_index=False).agg(
    average_temperature_c=("temperature_c", "mean"),
    average_speed_rpm=("rotational_speed_rpm", "mean"),
    average_torque_nm=("torque_nm", "mean"),
    average_tool_wear_min=("tool_wear_min", "mean"),
    failure_count=("failure_next_period", "sum"),
)
summary.to_csv(OUTPUT_FOLDER / "machine_summary.csv", index=False)
print("Machine summary:")
print(summary.round(2).to_string(index=False))

# Choose sensor columns as model inputs and the synthetic failure flag as the target.
feature_columns = ["temperature_c", "rotational_speed_rpm", "torque_nm", "tool_wear_min"]
features = data[feature_columns]
labels = data["failure_next_period"]

# Use stratification so the training and test sets have similar failure proportions.
X_train, X_test, y_train, y_test = train_test_split(
    features, labels, test_size=0.25, random_state=42, stratify=labels
)

# Train a straightforward Random Forest model.
model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight="balanced", n_jobs=-1)
model.fit(X_train, y_train)

# Predict failures for the held-back test examples.
predictions = model.predict(X_test)
report = "SYNTHETIC DEMO ONLY\n" + classification_report(y_test, predictions, zero_division=0)
print(report)
(OUTPUT_FOLDER / "model_report.txt").write_text(report, encoding="utf-8")

# Save feature importance so we can see which inputs the model used most.
importance = pd.DataFrame({"feature": feature_columns, "importance": model.feature_importances_})
importance = importance.sort_values("importance", ascending=False)
importance.to_csv(OUTPUT_FOLDER / "feature_importance.csv", index=False)

# Draw a bar chart of the feature importance values.
plt.figure(figsize=(8, 5))
plt.bar(importance["feature"], importance["importance"])
plt.title("Feature Importance - Synthetic Machine Data")
plt.xlabel("Sensor feature")
plt.ylabel("Importance")
plt.xticks(rotation=25, ha="right")
plt.tight_layout()
plt.savefig(OUTPUT_FOLDER / "feature_importance.png")
plt.close()

# Draw a confusion matrix to inspect the test predictions.
ConfusionMatrixDisplay.from_predictions(y_test, predictions, display_labels=["No failure", "Failure"])
plt.title("Machine Failure Demo - Confusion Matrix")
plt.tight_layout()
plt.savefig(OUTPUT_FOLDER / "confusion_matrix.png")
plt.close()

print("Finished. These are artificial examples, not a real predictive-maintenance system.")
