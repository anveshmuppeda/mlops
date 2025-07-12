import pandas as pd
import numpy as np
import json
import random
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Number of records
num_records = 20000

# Generate random data
data = {
    "id": np.arange(1, num_records + 1),
    "name": [f"Name_{i}" for i in np.random.randint(1, 1000, num_records)],
    "age": np.random.randint(18, 80, num_records),
    "salary": np.random.choice([50000, 60000, 70000, None], num_records),
    "hire_date": [
        (datetime.now() - timedelta(days=random.randint(0, 3650))).strftime("%Y-%m-%d")
        if random.random() > 0.1 else None
        for _ in range(num_records)
    ],
    "profile": [
        json.dumps({
            "address": f"Street {random.randint(1, 100)}, City {random.randint(1, 50)}",
            "phone": f"{random.randint(1000000000, 9999999999)}",
            "email": f"email_{random.randint(1, 1000)}@example.com"
        })
        if random.random() > 0.1 else None
        for _ in range(num_records)
    ],
    "department": np.random.choice(["HR", "IT", "Finance", "Marketing", None], num_records),
    "bonus": [None if random.random() > 0.9 else random.randint(1000, 10000) for _ in range(num_records)]
}

# Create DataFrame
df = pd.DataFrame(data)

# Introduce some NaN values randomly
df.loc[np.random.choice(df.index, size=int(num_records * 0.05), replace=False), "age"] = np.nan
df.loc[np.random.choice(df.index, size=int(num_records * 0.1), replace=False), "salary"] = np.nan

# Save to CSV
df.to_csv("mock_data.csv", index=False)