# 1. Hate Speech Detection

## Goal
Train a basic text classifier to distinguish between examples labelled `0` (not hateful in this dataset) and `1` (hateful in this dataset).

## Data
`data/hate_speech_demo.csv` has 1,600 generated text examples. The labels reflect the simple templates used in the dataset and do not represent a robust definition of hate speech in a more real life scenario

## Run
```bash
python -m pip install -r ../requirements.txt
python analyse_text.py
```

The script splits data into training and testing parts, turns text into numeric TF-IDF features, trains Logistic Regression, and reports accuracy and a classification report. It saves a confusion-matrix chart and a text report to `outputs/`.

## Limitations
Real language is nuanced. Models can mislabel reclaimed language, quotations, sarcasm, dialects, and discussion of harmful language. A more robust dataset can help in a real life application.