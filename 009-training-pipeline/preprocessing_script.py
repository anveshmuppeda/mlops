import pandas as pd
import sys
import os
import json
import numpy as np
from datetime import datetime
from sklearn.model_selection import train_test_split

# Load dataset
try:
    df = pd.read_csv('/opt/ml/processing/input/mock_data.csv')
    print(f"✅ Dataset loaded successfully!")
    print(f"📏 Dataset shape: {df.shape}")
except FileNotFoundError:
    print("❌ Error: mock_data.csv not found. Please run create_dataset.py first.")
    exit()

# Analyze missing patterns
print("\n📊 Missing Value Patterns:")
print("Missing Age values:")
print(df[df['age'].isnull()][['age', 'salary', 'department']])

print("Missing Salary values")
print(df[df['salary'].isnull()][['age', 'salary', 'department']])

# Get the median values for age, and salary
age_median = df['age'].median()
salary_median = df['salary'].median()
print("Age Median", age_median)
print("Salary Median", salary_median)

# Fill missing values of age with age_median
df['age'] = df['age'].fillna(age_median)
# Fill missing values of salary with salary_median
df['salary'] = df['salary'].fillna(salary_median)

# Verify the Age & Salary data
df.head()
# Check for missing values
print("Missing values in each column")
df.isnull().sum()

print("Print the missing values for Department\n")
print("Missing Department Missing values")
print(df[df['department'].isnull()][['age', 'salary', 'department']])

# Fill the missing values in department with 'Unknown'
df['department'] = df['department'].fillna('Unknown')

# Verify the Age & Salary data
df.head()
# Check for missing values
print("Missing values in each column")
print(df.isnull().sum())
# Check unique values in the department column
df['department'].unique()

print("Top rows from profile column \n")
print(df['profile'].head())

# Find the first non-null value in the column
profile_first_value = df['profile'].dropna().iloc[0]
# Print its type
print("\nProfile column values current data type")
print(type(profile_first_value))

# If your 'profile' column already contains Python dictionaries, not JSON strings.
# You do not need to parse it with json.loads(). The data is ready to be used directly.

# Convert profile JSON strings into dictionaries
df['profile'] = df['profile'].apply(lambda x: json.loads(x) if pd.notnull(x) else {})

# Extract Address Field
print("Extract Address Field....\n")
# Create new 'address' column by extracting from 'profile' dictionaries
df['address'] = df['profile'].apply(lambda x: x.get('address', None))  # Returns None if no address key

print("Top rows from profile column \n")
print(df['profile'].head())
print("\nTop rows from newly created address column \n")
print(df['address'].head())

# Extract Phone Field
print("Extract Phone Field....\n")
# Create new 'phone' column by extracting from 'profile' dictionaries
df['phone'] = df['profile'].apply(lambda x: x.get('phone', None))  # Returns None if no address key

print("Top rows from profile column \n")
print(df['profile'].head())
print("\nTop rows from newly created phone column \n")
print(df['phone'].head())

# Extract Email Field
print("Extract Email Field....\n")
# Create new 'email' column by extracting from 'profile' dictionaries
df['email'] = df['profile'].apply(lambda x: x.get('email', None))  # Returns None if no address key

print("Top rows from profile column \n")
print(df['profile'].head())
print("\nTop rows from newly created email column \n")
print(df['email'].head())

print(f"\n✅ Profile fields extracted:")


# Now drop the profile column
print("\nColumns before dropping profile:")
print(df.columns.tolist())

# Without inplace=True (df remains unchanged)
cleaned_df = df.drop(columns=['profile'])

# With inplace=True (df is modified directly)
#df.drop(columns=['profile'], inplace=True)

print("\nColumns in new DataFrame after dropping profile:")
# print(df.columns.tolist())
print(cleaned_df.columns.tolist())

print("\n💾 Saving cleaned data to: 'data/cleaned_data.csv' ...")
cleaned_df.to_csv("/opt/ml/processing/output/cleaned_data.csv", index=False)
print("✅ Cleaned data saved to: '/opt/ml/processing/output/cleaned_data.csv'")

transform_df = pd.read_csv('/opt/ml/processing/output/cleaned_data.csv')
transform_df.head()

# Create a new column 'address_length' 
print("\n🔧 Creating Address Length Feature...")
transform_df['address_length'] = transform_df['address'].apply(lambda x: len(str(x)))
print("Address followed by Address Length columns")
transform_df[['address', 'address_length']].head()

print("\n🔧 Creating Salary Categories...")
# Define the bins and labels
bins = [0, 50000, 70000, 100000]
labels = ['low', 'medium', 'high']

# Create a new column 'salary_category'
transform_df['salary_category'] = pd.cut(df['salary'], bins=bins, labels=labels, include_lowest=True)

# Print sample data after adding the 'salary_category' column
print("Sample data after adding the 'salary_category' column: \n")
transform_df[['salary', 'salary_category']].head()

print("\n🔧 Creating Age Groups...")
# Define age bins and labels
age_bins = [0, 25, 35, 45, 55, float('inf')]
age_labels = ['Young', 'Early Career', 'Mid Career', 'Senior', 'Experienced']

# Create a new column 'salary_category'
transform_df['age_group'] = pd.cut(df['age'], bins=age_bins, labels=age_labels, include_lowest=True)

# Age group distribution
print(f"Age group distribution:")
print(transform_df['age_group'].value_counts())

# Print sample data after adding the 'salary_category' column
print("\nSample data after adding the 'age_group' column: \n")
transform_df[['age', 'age_group']].head()

# Check for missing values
print("\n❓ Missing Values Analysis before Removing Missing:\n")
print(transform_df.isnull().sum())

# Remove missing rows for bonus
transform_df = transform_df[transform_df['bonus'].notna()]
print("\n❓ Missing Values Analysis after Removing Missing:\n")
transform_df.isnull().sum()


transform_df = pd.get_dummies(transform_df, columns=['department', 'age_group', 'salary_category'], prefix=['dept', 'age', 'salary'])
print("Top 5 rows with boolean values")
print(transform_df.head())

bool_cols = transform_df.select_dtypes(include='bool').columns
transform_df[bool_cols] = transform_df[bool_cols].astype(int)

print("\nTop 5 rows with numberic values\n")
print(transform_df.head())

print("Convert hire_date to datetime")
transform_df['hire_date'] = pd.to_datetime(transform_df['hire_date'], errors='coerce')
print(transform_df['hire_date'].head())
# print(transform_df.dtypes)

# non_date_rows = transform_df[transform_df['hire_date'].apply(lambda x: isinstance(x, str))]
# print("non date rows:")
# print(non_date_rows)

print("Calculate Tenure in Days....")
transform_df['tenure_days'] = (pd.Timestamp('now') - transform_df['hire_date']).dt.days

print("Calculated Tenure Days")
print(transform_df['tenure_days'])

print("Handle Missing values of tenure_days")
transform_df['tenure_days'] = transform_df['tenure_days'].fillna(transform_df['tenure_days'].median())

print("Tenure Days after handled missing days")
print(transform_df['tenure_days'])



print("Dropping ID, Address, Phone, Name, Hire Date, and Email.....")
transform_df.drop(columns=['id', 'address', 'phone', 'email', 'name', 'hire_date'], inplace=True)
print("After dropping ID, Address, Phone, Name, Hire Date, and Email, dataset look like")
print(transform_df.head())


print("Saving Transformed data csv to: '/opt/ml/processing/output/transformed_data.csv' ...")
transform_df.to_csv("/opt/ml/processing/output/transformed_data.csv", index=False)
print("\nTransformed data csv saved to: '/opt/ml/processing/output/transformed_data.csv'")
