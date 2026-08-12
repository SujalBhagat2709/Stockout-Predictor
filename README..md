# Stockout Predictor

## Overview

Stockout Predictor is a Python application that estimates when products may run out of inventory.

The system uses current stock, recent daily sales, and supplier lead time to estimate how many days of inventory remain and determine whether a reorder may be required.

## Features

- Product Analysis
- Average Daily Sales Calculation
- Estimated Stockout Date/Time
- Supplier Lead-Time Comparison
- Stock Risk Classification
- Reorder Recommendation
- Highest-Risk Product Detection
- Inventory Summary

## Project Structure

stockout-predictor/

├── stockout_predictor.py
├── stockout_studio.py
├── README.md
└── .gitignore

## Requirements

- Python 3.x
- No external libraries required

## Run

```bash
python stockout_studio.py
