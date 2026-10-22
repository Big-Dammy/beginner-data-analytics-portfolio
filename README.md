[README.md](https://github.com/user-attachments/files/33814419/README.md)
# Six Beginner-Friendly Data Analytics Projects

A portfolio of six small, documented projects designed to help a beginner coding skills. The Python is intentionally straightforward, with comments explaining the steps. All included datasets are for learning; they may not totally represent what real customers, patients, cardholders, or factory equipment look like but definitely reflect each possible case scenario

## Projects
1. **Hate Speech Detection**  text classification using TF-IDF and Logistic Regression.
2. **Anomaly Detection**  find unusual sensor readings using a simple z-score rule.
3. **Retail Sales Analysis**  explore 50,000 synthetic transactions with pandas and charts.
4. **Credit Card Fraud Detection**  learn about imbalanced classification and precision/recall.
5. **Simple File Automation**  safely organise files in a demo folder, with dry-run mode by default.
6. **Manufacturing Machine Monitoring**  explore synthetic sensor data and a basic failure model.

## Run the projects
Use Python 3.10 or newer. From a terminal, open this folder and run:

```bash
python -m pip install -r requirements.txt
python 01_hate_speech_detection/analyse_text.py
python 02_anomaly_detection/detect_anomalies.py
python 03_retail_sales_analysis/analyse_sales.py
python 04_credit_card_fraud_detection/detect_fraud.py
python 05_simple_automation/organise_files.py
python 06_manufacturing_monitoring/monitor_machines.py
```

Each script reads the included CSV data and writes outputs into that project's `outputs/` folder. The automation project only works inside its own `demo_inbox/` folder. It previews actions unless you explicitly add `--apply`.
