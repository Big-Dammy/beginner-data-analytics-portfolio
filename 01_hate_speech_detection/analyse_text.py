# Import the tools we need for splitting data, turning words into numbers,
# training a model, checking results, and drawing a simple chart.
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay

# Find the folder where this Python file lives, so the script works from any folder.
HERE = Path(__file__).resolve().parent
DATA_FILE = HERE / "data" / "hate_speech_demo.csv"
OUTPUT_FOLDER = HERE / "outputs"
OUTPUT_FOLDER.mkdir(exist_ok=True)

# Read the sample data from a CSV file.
data = pd.read_csv(DATA_FILE)

# Separate the written text (input) from the label we want the model to predict.
texts = data["text"].fillna("")
labels = data["label"]

# Keep some examples aside so we can test on examples the model did not train on.
train_text, test_text, train_labels, test_labels = train_test_split(
    texts, labels, test_size=0.25, random_state=42, stratify=labels
)

# Convert words into numeric features that a machine-learning model can understand.
# TF-IDF gives more weight to words that are useful within this small dataset.
vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=3000)
train_numbers = vectorizer.fit_transform(train_text)
test_numbers = vectorizer.transform(test_text)

# Create a simple Logistic Regression classifier and teach it from training examples.
model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(train_numbers, train_labels)

# Ask the model to predict the labels for the held-back test examples.
predictions = model.predict(test_numbers)

# Calculate accuracy and create a readable report of the results.
accuracy = accuracy_score(test_labels, predictions)
report = classification_report(test_labels, predictions, zero_division=0)
report_text = f"DEMO RESULTS ONLY - synthetic dataset\nAccuracy: {accuracy:.3f}\n\n{report}"
print(report_text)
(OUTPUT_FOLDER / "classification_report.txt").write_text(report_text, encoding="utf-8")

# Draw a confusion matrix so we can see correct and incorrect predictions by class.
ConfusionMatrixDisplay.from_predictions(test_labels, predictions)
plt.title("Hate Speech Demo - Confusion Matrix")
plt.tight_layout()
plt.savefig(OUTPUT_FOLDER / "confusion_matrix.png")
plt.close()

# Save a small file with predictions to make the result easy to inspect.
preview = pd.DataFrame({"text": test_text.reset_index(drop=True), "actual_label": test_labels.reset_index(drop=True), "predicted_label": predictions})
preview.head(100).to_csv(OUTPUT_FOLDER / "prediction_sample.csv", index=False)
print("Finished. Check the outputs folder. Remember: this is synthetic demo data.")
