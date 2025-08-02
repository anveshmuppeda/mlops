import pandas as pd
import sys
import os
import json
import numpy as np
from datetime import datetime
from sklearn.model_selection import train_test_split

# Load dataset
try:
    df = pd.read_csv('/opt/ml/processing/input/transformed_data.csv')
    print(f"✅ Transformed Data loaded successfully!")
    print(f"📏 Dataset shape: {df.shape}")
except FileNotFoundError:
    print("❌ Error: transformed_data.csv not found. Please check Pre Processing step logs...")
    exit()

# Separate features and target
X = df.drop(columns=['bonus'])  # Drop the target column from the features
y = df['bonus']

# Split the data into train (70%), validation (20%), and test (10%)
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.33, random_state=42)

print(f"Training set: {X_train.shape[0]} samples")
print(f"Validation set: {X_val.shape[0]} samples")
print(f"Test set: {X_test.shape[0]} samples")

# Save the datasets to CSV
train_data = pd.concat([y_train, X_train], axis=1)
val_data = pd.concat([y_val, X_val], axis=1)
test_data = pd.concat([y_test, X_test], axis=1)

# Save locally
os.makedirs('data', exist_ok=True)

train_data.to_csv('/opt/ml/processing/train/train.csv', index=False, header=False)
val_data.to_csv('/opt/ml/processing/validation/validation.csv', index=False, header=False)
test_data.to_csv('/opt/ml/processing/test/test.csv', index=False)
