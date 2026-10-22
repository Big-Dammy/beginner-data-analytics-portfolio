# Import Path for file locations, pandas for tables, and matplotlib for a chart.
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Build file paths relative to this script, not to the terminal's current folder.
HERE = Path(__file__).resolve().parent
DATA_FILE = HERE / "data" / "sensor_readings.csv"
OUTPUT_FOLDER = HERE / "outputs"
OUTPUT_FOLDER.mkdir(exist_ok=True)

# Load the readings from the CSV file.
data = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])

# Calculate the average and standard deviation of the sensor readings.
average = data["sensor_value"].mean()
standard_deviation = data["sensor_value"].std()

# Calculate a z-score for every reading. If standard deviation is zero,
# use zero z-scores to avoid dividing by zero.
if standard_deviation == 0:
    data["z_score"] = 0
else:
    data["z_score"] = (data["sensor_value"] - average) / standard_deviation

# Flag readings more than three standard deviations from the average.
data["is_anomaly"] = data["z_score"].abs() > 3
anomalies = data[data["is_anomaly"]].copy()

# Save all flagged rows so a person can investigate them.
anomalies.to_csv(OUTPUT_FOLDER / "flagged_anomalies.csv", index=False)

# Draw the readings and mark flagged values with a different symbol.
plt.figure(figsize=(12, 5))
plt.plot(data["timestamp"], data["sensor_value"], linewidth=0.7, label="Sensor reading")
plt.scatter(anomalies["timestamp"], anomalies["sensor_value"], s=18, label="Flagged anomaly")
plt.axhline(average, linestyle="--", label="Average")
plt.title("Synthetic Sensor Readings and Flagged Anomalies")
plt.xlabel("Time")
plt.ylabel("Sensor value")
plt.legend()
plt.tight_layout()
plt.savefig(OUTPUT_FOLDER / "anomaly_chart.png")
plt.close()

# Print a short summary for the terminal.
print(f"Rows checked: {len(data):,}")
print(f"Average sensor value: {average:.2f}")
print(f"Flagged anomalies: {len(anomalies):,}")
print("Finished. These are synthetic readings, not real equipment data.")
