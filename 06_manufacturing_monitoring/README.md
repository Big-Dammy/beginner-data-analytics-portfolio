# 6. Manufacturing Machine Monitoring

## Goal
Explore machine sensor measurements and train a basic model to predict a synthetic failure label.

## Data
12,000 machine readings with temperature, rotational speed, torque, tool wear, and a `failure_next_period` label. 

## Run
`python monitor_machines.py`

The script summarises readings by machine, trains a Random Forest classifier, prints a classification report, saves feature importance, and writes a chart.

## Limitations
Real manufacturing failures are relatively rare and depend on maintenance history, machine type, process conditions, and time. This simple dataset does not model those complexities. Do not use the model to make safety or maintenance decisions as various scenarios may need a different approach.
