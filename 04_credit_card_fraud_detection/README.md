# 4. Credit Card Fraud Detection

## Goal
Learn why fraud detection is an imbalanced classification problem and why accuracy alone can be misleading.

## Data
20,000 transactions, with roughly 2.5% labelled fraud. All fields are labelled as required

## Run
`python detect_fraud.py`

The script uses a stratified train/test split, a Random Forest classifier, and reports precision, recall, F1, average precision, and a confusion matrix. The output folder contains a report, a confusion-matrix chart, and a sample of predictions.

## Why precision and recall?
A model can achieve high accuracy by predicting that nearly every transaction is legitimate. Precision asks how many flagged transactions were actually labelled fraud; recall asks how many labelled fraud cases were found. In real systems, false alarms and missed fraud both have costs.

## Limitations
With respect to the used dataset, scores only show that the code runs. Real fraud detection needs secure, lawful data handling, careful validation, monitoring, and specialist review and possibly a more roburst dataset.
