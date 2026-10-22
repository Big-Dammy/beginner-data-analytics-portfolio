# 2. Anomaly Detection

## Goal
Find sensor values that are unusually far from the average using a z-score rule.

## Data
12,000 generated sensor readings with a few artificial spikes. The spikes in the dataset helps with the subject of the matter

## Run
`python detect_anomalies.py`

The script saves flagged rows and a chart to `outputs/`. A z-score is the number of standard deviations a value is away from the average. This project flags absolute z-scores above 3.

## Limitations
A simple global average can miss slow changes and may flag normal values when data is seasonal or has multiple operating modes. Always investigate alerts in context.
