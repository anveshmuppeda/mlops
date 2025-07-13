import pandas as pd
import json
import numpy as np
from datetime import datetime
print("\n🔧 Creating Salary Categories...")
# Define the bins and labels
bins = [0, 50000, 70000, 100000]
labels = ['low', 'medium', 'high']

# Create a new column 'salary_category'
df['salary_category'] = pd.cut(df['salary'], bins=bins, labels=labels, include_lowest=True)

# Print sample data after adding the 'salary_category' column
print("Sample data after adding the 'salary_category' column: \n")
df[['salary', 'salary_category']].head()
