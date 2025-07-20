```python
print("🚀 Starting Data Transformation Pipeline")
print("=" * 50)
```

    🚀 Starting Data Transformation Pipeline
    ==================================================


# MLOps Data Transformation Pipeline
`This notebook demonstrates key data transformation techniques commonly used in machine learning pipelines. It follows MLOps best practices for data preprocessing and feature engineering.`

## Prepare Environment
### Install Dependencies
**Install pandas library uisng the below command**  
The following packages are required for this data transformation pipeline:  
- pandas: Data manipulation and analysis

Note: The **!** tells Jupyter to run this as a command in your system's shell



```python
print("Installing pandas")
!pip install pandas
```

    Installing pandas
    Requirement already satisfied: pandas in ./createds/lib/python3.13/site-packages (2.3.1)
    Requirement already satisfied: numpy>=1.26.0 in ./createds/lib/python3.13/site-packages (from pandas) (2.3.1)
    Requirement already satisfied: python-dateutil>=2.8.2 in ./createds/lib/python3.13/site-packages (from pandas) (2.9.0.post0)
    Requirement already satisfied: pytz>=2020.1 in ./createds/lib/python3.13/site-packages (from pandas) (2025.2)
    Requirement already satisfied: tzdata>=2022.7 in ./createds/lib/python3.13/site-packages (from pandas) (2025.2)
    Requirement already satisfied: six>=1.5 in ./createds/lib/python3.13/site-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)


### Create Dataset
Generate mock dataset using the create_dataset.py script.  
This ensures reproducible data for our transformation pipeline.  


```python
!python3 create_dataset.py
```

### Import Required Libraries


```python
import pandas as pd
import json
import numpy as np
from datetime import datetime
```

## 1. Data Exploration  
Load the raw dataset and perform initial data profiling. 
This step is crucial for understanding data quality and structure. 

### Step 1: Load the CSV File into the DataFrame


```python
try:
    df = pd.read_csv("data/mock_data.csv")
    print(f"✅ Dataset loaded successfully!")
    print(f"📏 Dataset shape: {df.shape}")
except FileNotFoundError:
    print("❌ Error: mock_data.csv not found. Please run create_dataset.py first.")
    exit()
```

    ✅ Dataset loaded successfully!
    📏 Dataset shape: (20000, 8)


### Step 2: Analyse the Data  
Perform comprehensive data analysis to understand:
- Data types and memory usage
- Missing values pattern
- Statistical distribution
- Unique values and categories


```python
# Display the first 5 rows from the loaded DataFrame
print("\n📋 First 5 rows:")
df.head()
```

    
    📋 First 5 rows:





<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>age</th>
      <th>salary</th>
      <th>hire_date</th>
      <th>profile</th>
      <th>department</th>
      <th>bonus</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Name_103</td>
      <td>77.0</td>
      <td>60000.0</td>
      <td>2024-03-31</td>
      <td>{"address": "Street 5, City 17", "phone": "312...</td>
      <td>Marketing</td>
      <td>6842.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Name_436</td>
      <td>62.0</td>
      <td>50000.0</td>
      <td>2017-09-10</td>
      <td>NaN</td>
      <td>Marketing</td>
      <td>4001.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Name_861</td>
      <td>61.0</td>
      <td>60000.0</td>
      <td>2021-06-19</td>
      <td>{"address": "Street 25, City 41", "phone": "23...</td>
      <td>HR</td>
      <td>7335.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Name_271</td>
      <td>36.0</td>
      <td>70000.0</td>
      <td>2024-08-24</td>
      <td>{"address": "Street 96, City 50", "phone": "80...</td>
      <td>NaN</td>
      <td>5666.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Name_107</td>
      <td>78.0</td>
      <td>60000.0</td>
      <td>2025-02-15</td>
      <td>{"address": "Street 41, City 45", "phone": "57...</td>
      <td>IT</td>
      <td>9527.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Get the summary of the DataFrame
print("\n📊 Data Types & Non-Null Counts:\n")
df.info()
```

    
    📊 Data Types & Non-Null Counts:
    
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 20000 entries, 0 to 19999
    Data columns (total 8 columns):
     #   Column      Non-Null Count  Dtype  
    ---  ------      --------------  -----  
     0   id          20000 non-null  int64  
     1   name        20000 non-null  object 
     2   age         19000 non-null  float64
     3   salary      13519 non-null  float64
     4   hire_date   18025 non-null  object 
     5   profile     17957 non-null  object 
     6   department  16003 non-null  object 
     7   bonus       17999 non-null  float64
    dtypes: float64(3), int64(1), object(4)
    memory usage: 1.2+ MB



```python
# Check for duplicate rows
duplicates = df.duplicated().sum()
print(f"\n🔄 Duplicate rows: {duplicates}")
```

    
    🔄 Duplicate rows: 0



```python
# Check unique values in the department column
df['department'].unique()
```




    array(['Marketing', 'HR', nan, 'IT', 'Finance'], dtype=object)




```python
# View statistical summary for numeric coloums
print("\n📈 Statistical Summary:")
df.describe(include='all')
```

    
    📈 Statistical Summary:





<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>age</th>
      <th>salary</th>
      <th>hire_date</th>
      <th>profile</th>
      <th>department</th>
      <th>bonus</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>20000.000000</td>
      <td>20000</td>
      <td>19000.000000</td>
      <td>13519.000000</td>
      <td>18025</td>
      <td>17957</td>
      <td>16003</td>
      <td>17999.000000</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>NaN</td>
      <td>999</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3628</td>
      <td>17957</td>
      <td>4</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>top</th>
      <td>NaN</td>
      <td>Name_825</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2024-02-17</td>
      <td>{"address": "Street 5, City 17", "phone": "312...</td>
      <td>IT</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>NaN</td>
      <td>37</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>13</td>
      <td>1</td>
      <td>4058</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>10000.500000</td>
      <td>NaN</td>
      <td>48.444684</td>
      <td>59962.275316</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>5523.213012</td>
    </tr>
    <tr>
      <th>std</th>
      <td>5773.647028</td>
      <td>NaN</td>
      <td>17.892848</td>
      <td>8200.588356</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2588.660406</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>NaN</td>
      <td>18.000000</td>
      <td>50000.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1000.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>5000.750000</td>
      <td>NaN</td>
      <td>33.000000</td>
      <td>50000.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3293.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>10000.500000</td>
      <td>NaN</td>
      <td>48.000000</td>
      <td>60000.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>5553.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>15000.250000</td>
      <td>NaN</td>
      <td>64.000000</td>
      <td>70000.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>7774.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>20000.000000</td>
      <td>NaN</td>
      <td>79.000000</td>
      <td>70000.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>10000.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Check for missing values
print("\n❓ Missing Values Analysis:\n")
df.isnull().sum()
```

    
    ❓ Missing Values Analysis:
    





    id               0
    name             0
    age           1000
    salary        6481
    hire_date     1975
    profile       2043
    department    3997
    bonus         2001
    dtype: int64



## 🧹 2. Data Cleaning & Quality Improvement

### Step 1: Handle Missing values of age, and salary
Handle missing values in age and salary columns using appropriate strategies:
- For age: Use median (robust to outliers)
- For salary: Use median (robust to outliers)


```python
# Analyze missing patterns
print("\n📊 Missing Value Patterns:")
print("Missing Age values:")
print(df[df['age'].isnull()][['age', 'salary', 'department']])
```

    
    📊 Missing Value Patterns:
    Missing Age values:
           age   salary department
    44     NaN  60000.0  Marketing
    115    NaN  60000.0         IT
    127    NaN      NaN  Marketing
    147    NaN  60000.0         HR
    164    NaN  70000.0         IT
    ...    ...      ...        ...
    19872  NaN  60000.0         HR
    19921  NaN      NaN         HR
    19940  NaN  70000.0        NaN
    19997  NaN  60000.0         IT
    19998  NaN  60000.0  Marketing
    
    [1000 rows x 3 columns]



```python
print("Missing Salary values")
print(df[df['salary'].isnull()][['age', 'salary', 'department']])
```

    Missing Salary values
            age  salary department
    5      35.0     NaN         IT
    11     61.0     NaN         IT
    13     46.0     NaN        NaN
    14     48.0     NaN         IT
    15     61.0     NaN         HR
    ...     ...     ...        ...
    19984  71.0     NaN        NaN
    19988  72.0     NaN  Marketing
    19992  60.0     NaN        NaN
    19993  76.0     NaN  Marketing
    19999  47.0     NaN        NaN
    
    [6481 rows x 3 columns]



```python
# Get the median values for age, and salary
age_median = df['age'].median()
salary_median = df['salary'].median()
print("Age Median", age_median)
print("Salary Median", salary_median)
```

    Age Median 48.0
    Salary Median 60000.0



```python
# Fill missing values of age with age_median
df['age'] = df['age'].fillna(age_median)
# Fill missing values of salary with salary_median
df['salary'] = df['salary'].fillna(salary_median)
```

#### Age & Salary columns missing values are filled with the respective median


```python
# Verify the Age & Salary data
df.head()
# Check for missing values
print("Missing values in each column")
df.isnull().sum()
```

    Missing values in each column





    id               0
    name             0
    age              0
    salary           0
    hire_date     1975
    profile       2043
    department    3997
    bonus         2001
    dtype: int64



### Step 2: Handle Missing values of Department
Handle missing values in categorical columns:
- For department: Use 'Unknown' category
- This preserves the information that the department was missing


```python
print("Print the missing values for Department\n")
print("Missing Department Missing values")
print(df[df['department'].isnull()][['age', 'salary', 'department']])
```

    Print the missing values for Department
    
    Missing Department Missing values
            age   salary department
    3      36.0  70000.0        NaN
    13     46.0  60000.0        NaN
    49     34.0  50000.0        NaN
    53     33.0  60000.0        NaN
    57     28.0  70000.0        NaN
    ...     ...      ...        ...
    19973  50.0  60000.0        NaN
    19975  29.0  60000.0        NaN
    19984  71.0  60000.0        NaN
    19992  60.0  60000.0        NaN
    19999  47.0  60000.0        NaN
    
    [3997 rows x 3 columns]



```python
# Fill the missing values in department with 'Unknown'
df['department'] = df['department'].fillna('Unknown')
```

#### Department column missing values are filled with the respective median


```python
# Verify the Age & Salary data
df.head()
# Check for missing values
print("Missing values in each column")
print(df.isnull().sum())
# Check unique values in the department column
df['department'].unique()
```

    Missing values in each column
    id               0
    name             0
    age              0
    salary           0
    hire_date     1975
    profile       2043
    department       0
    bonus         2001
    dtype: int64





    array(['Marketing', 'HR', 'Unknown', 'IT', 'Finance'], dtype=object)



### Step 3: Parse and Extract Profile Information
Devide Profile Column into 3 different columns i.e., Address, Phone, Email   

Parse JSON profile data and extract structured information:
- Extract address, phone, and email into separate columns
- Handle malformed JSON gracefully
- Maintain data integrity during extraction


```python
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
```

    Top rows from profile column 
    
    0    {"address": "Street 5, City 17", "phone": "312...
    1                                                  NaN
    2    {"address": "Street 25, City 41", "phone": "23...
    3    {"address": "Street 96, City 50", "phone": "80...
    4    {"address": "Street 41, City 45", "phone": "57...
    Name: profile, dtype: object
    
    Profile column values current data type
    <class 'str'>



```python
# Extract Address Field
print("Extract Address Field....\n")
# Create new 'address' column by extracting from 'profile' dictionaries
df['address'] = df['profile'].apply(lambda x: x.get('address', None))  # Returns None if no address key

print("Top rows from profile column \n")
print(df['profile'].head())
print("\nTop rows from newly created address column \n")
print(df['address'].head())

```

    Extract Address Field....
    
    Top rows from profile column 
    
    0    {'address': 'Street 5, City 17', 'phone': '312...
    1                                                   {}
    2    {'address': 'Street 25, City 41', 'phone': '23...
    3    {'address': 'Street 96, City 50', 'phone': '80...
    4    {'address': 'Street 41, City 45', 'phone': '57...
    Name: profile, dtype: object
    
    Top rows from newly created address column 
    
    0     Street 5, City 17
    1                  None
    2    Street 25, City 41
    3    Street 96, City 50
    4    Street 41, City 45
    Name: address, dtype: object



```python
# Extract Phone Field
print("Extract Phone Field....\n")
# Create new 'phone' column by extracting from 'profile' dictionaries
df['phone'] = df['profile'].apply(lambda x: x.get('phone', None))  # Returns None if no address key

print("Top rows from profile column \n")
print(df['profile'].head())
print("\nTop rows from newly created phone column \n")
print(df['phone'].head())

```

    Extract Phone Field....
    
    Top rows from profile column 
    
    0    {'address': 'Street 5, City 17', 'phone': '312...
    1                                                   {}
    2    {'address': 'Street 25, City 41', 'phone': '23...
    3    {'address': 'Street 96, City 50', 'phone': '80...
    4    {'address': 'Street 41, City 45', 'phone': '57...
    Name: profile, dtype: object
    
    Top rows from newly created phone column 
    
    0    3125396991
    1          None
    2    2329140322
    3    8091272320
    4    5788036047
    Name: phone, dtype: object



```python
# Extract Email Field
print("Extract Email Field....\n")
# Create new 'email' column by extracting from 'profile' dictionaries
df['email'] = df['profile'].apply(lambda x: x.get('email', None))  # Returns None if no address key

print("Top rows from profile column \n")
print(df['profile'].head())
print("\nTop rows from newly created email column \n")
print(df['email'].head())

print(f"\n✅ Profile fields extracted:")
```

    Extract Email Field....
    
    Top rows from profile column 
    
    0    {'address': 'Street 5, City 17', 'phone': '312...
    1                                                   {}
    2    {'address': 'Street 25, City 41', 'phone': '23...
    3    {'address': 'Street 96, City 50', 'phone': '80...
    4    {'address': 'Street 41, City 45', 'phone': '57...
    Name: profile, dtype: object
    
    Top rows from newly created email column 
    
    0    email_268@example.com
    1                     None
    2    email_523@example.com
    3    email_954@example.com
    4    email_851@example.com
    Name: email, dtype: object
    
    ✅ Profile fields extracted:



```python
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
```

    
    Columns before dropping profile:
    ['id', 'name', 'age', 'salary', 'hire_date', 'profile', 'department', 'bonus', 'address', 'phone', 'email']
    
    Columns in new DataFrame after dropping profile:
    ['id', 'name', 'age', 'salary', 'hire_date', 'department', 'bonus', 'address', 'phone', 'email']


### Step 4: Save cleaned data into new CSV


```python
print("\n💾 Saving cleaned data to: 'data/cleaned_data.csv' ...")
cleaned_df.to_csv("data/cleaned_data.csv", index=False)
print("✅ Cleaned data saved to: 'data/cleaned_data.csv'")
```

    
    💾 Saving cleaned data to: 'data/cleaned_data.csv' ...
    ✅ Cleaned data saved to: 'data/cleaned_data.csv'


## 3. Data Transformation & Feature Engineering

### Step 1: Load the cleaned dataset into new DataFrame


```python
transform_df = pd.read_csv("data/cleaned_data.csv")
transform_df.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>age</th>
      <th>salary</th>
      <th>hire_date</th>
      <th>department</th>
      <th>bonus</th>
      <th>address</th>
      <th>phone</th>
      <th>email</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Name_103</td>
      <td>77.0</td>
      <td>60000.0</td>
      <td>2024-03-31</td>
      <td>Marketing</td>
      <td>6842.0</td>
      <td>Street 5, City 17</td>
      <td>3.125397e+09</td>
      <td>email_268@example.com</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Name_436</td>
      <td>62.0</td>
      <td>50000.0</td>
      <td>2017-09-10</td>
      <td>Marketing</td>
      <td>4001.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Name_861</td>
      <td>61.0</td>
      <td>60000.0</td>
      <td>2021-06-19</td>
      <td>HR</td>
      <td>7335.0</td>
      <td>Street 25, City 41</td>
      <td>2.329140e+09</td>
      <td>email_523@example.com</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Name_271</td>
      <td>36.0</td>
      <td>70000.0</td>
      <td>2024-08-24</td>
      <td>Unknown</td>
      <td>5666.0</td>
      <td>Street 96, City 50</td>
      <td>8.091272e+09</td>
      <td>email_954@example.com</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Name_107</td>
      <td>78.0</td>
      <td>60000.0</td>
      <td>2025-02-15</td>
      <td>IT</td>
      <td>9527.0</td>
      <td>Street 41, City 45</td>
      <td>5.788036e+09</td>
      <td>email_851@example.com</td>
    </tr>
  </tbody>
</table>
</div>



### Step 2 : Feature Engineering - Address Length
Create address length feature for potential geographic analysis.


```python
# Create a new column 'address_length' 
print("\n🔧 Creating Address Length Feature...")
transform_df['address_length'] = transform_df['address'].apply(lambda x: len(str(x)))
print("Address followed by Address Length columns")
transform_df[['address', 'address_length']].head()
```

    
    🔧 Creating Address Length Feature...
    Address followed by Address Length columns





<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>address</th>
      <th>address_length</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Street 5, City 17</td>
      <td>17</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Street 25, City 41</td>
      <td>18</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Street 96, City 50</td>
      <td>18</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Street 41, City 45</td>
      <td>18</td>
    </tr>
  </tbody>
</table>
</div>



### Step 3: Feature Engineering - Salary Categorization
Create salary categories for easier analysis and modeling.  
This converts continuous salary into ordinal categories.


```python
print("\n🔧 Creating Salary Categories...")
# Define the bins and labels
bins = [0, 50000, 70000, 100000]
labels = ['low', 'medium', 'high']

# Create a new column 'salary_category'
transform_df['salary_category'] = pd.cut(df['salary'], bins=bins, labels=labels, include_lowest=True)

# Print sample data after adding the 'salary_category' column
print("Sample data after adding the 'salary_category' column: \n")
transform_df[['salary', 'salary_category']].head()
```

    
    🔧 Creating Salary Categories...
    Sample data after adding the 'salary_category' column: 
    





<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>salary</th>
      <th>salary_category</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>60000.0</td>
      <td>medium</td>
    </tr>
    <tr>
      <th>1</th>
      <td>50000.0</td>
      <td>low</td>
    </tr>
    <tr>
      <th>2</th>
      <td>60000.0</td>
      <td>medium</td>
    </tr>
    <tr>
      <th>3</th>
      <td>70000.0</td>
      <td>medium</td>
    </tr>
    <tr>
      <th>4</th>
      <td>60000.0</td>
      <td>medium</td>
    </tr>
  </tbody>
</table>
</div>



### Step 4: Feature Engineering - Age Groups  
Create age groups for demographic analysis.  
This helps in understanding age-based patterns in the data.  


```python
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

```

    
    🔧 Creating Age Groups...
    Age group distribution:
    age_group
    Experienced     7318
    Senior          4068
    Early Career    3142
    Mid Career      3022
    Young           2450
    Name: count, dtype: int64
    
    Sample data after adding the 'age_group' column: 
    





<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>age_group</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>77.0</td>
      <td>Experienced</td>
    </tr>
    <tr>
      <th>1</th>
      <td>62.0</td>
      <td>Experienced</td>
    </tr>
    <tr>
      <th>2</th>
      <td>61.0</td>
      <td>Experienced</td>
    </tr>
    <tr>
      <th>3</th>
      <td>36.0</td>
      <td>Mid Career</td>
    </tr>
    <tr>
      <th>4</th>
      <td>78.0</td>
      <td>Experienced</td>
    </tr>
  </tbody>
</table>
</div>



### Step 5: Aggregation Features - Department Statistics  
Create department-level aggregations for comparative analysis.  
This enables understanding of department-wise patterns.  


```python
print("\n🔧 Creating Department Statistics...")
# Group by 'department' and calculate average salary and age
department_summary_report = df.groupby('department').agg({
    'salary': 'mean',
    'age': 'mean'
}).reset_index()

# rename columns of department_summary_report for clarity
department_summary_report.columns = ['Department', 'Average Salary', 'Average Age']
```

    
    🔧 Creating Department Statistics...



```python
# Print the Summary Report
print("Summary report of average salary and age based on the department:\n")
print(department_summary_report)
```

    Summary report of average salary and age based on the department:
    
      Department  Average Salary  Average Age
    0    Finance    59830.035515    48.345256
    1         HR    60015.155342    48.620106
    2         IT    60034.499754    48.650074
    3  Marketing    60049.455984    48.419139
    4    Unknown    59939.954966    48.075056


### Step 6: Data Quality Metrics
Calculate data quality metrics for monitoring and MLOps.  
These metrics help track data drift and quality over time.  



```python

print("\n📊 Data Quality Metrics...")

quality_metrics = {
    'total_rows': len(transform_df),
    'total_columns': len(transform_df.columns),
    'missing_values_count': transform_df.isnull().sum().sum(),
    'duplicate_rows': transform_df.duplicated().sum(),
    'numeric_columns': len(transform_df.select_dtypes(include=[np.number]).columns),
    'categorical_columns': len(transform_df.select_dtypes(include=['object']).columns),
    'unique_departments': transform_df['department'].nunique(),
    'unique_age_groups': transform_df['age_group'].nunique(),
    'unique_salary_categories': transform_df['salary_category'].nunique(),
    'processing_timestamp': datetime.now().isoformat()
}

print("Data Quality Metrics:")
for metric, value in quality_metrics.items():
    print(f"  {metric}: {value}")
```

    
    📊 Data Quality Metrics...
    Data Quality Metrics:
      total_rows: 20000
      total_columns: 13
      missing_values_count: 10105
      duplicate_rows: 0
      numeric_columns: 6
      categorical_columns: 5
      unique_departments: 5
      unique_age_groups: 5
      unique_salary_categories: 2
      processing_timestamp: 2025-07-12T19:14:18.609496


### Step 7: Save the transformed DataFrame to a new csv file


```python
print("Saving Transformed data csv to: 'data/transformed_data.csv' ...")
transform_df.to_csv("data/transformed_data.csv", index=False)
print("\nTransformed data csv saved to: 'data/transformed_data.csv'")
```

    Saving Transformed data csv to: 'data/transformed_data.csv' ...
    
    Transformed data csv saved to: 'data/transformed_data.csv'



```python
### Step 2: Save Department Statistics
print("Saving department statistics...")
department_summary_report.to_csv("data/department_statistics.csv", index=False)
print("✅ Department statistics saved to: 'data/department_statistics.csv'")


```

    Saving department statistics...
    ✅ Department statistics saved to: 'data/department_statistics.csv'


## 4. Next Steps for MLOps


```python
print(f"\n🎯 Next Steps for MLOps:")
print(f"  1. Model training using transformed features")
print(f"  2. Model validation and testing")
print(f"  3. Model deployment and monitoring")
print(f"  4. Data drift monitoring using quality metrics")
print(f"  5. Pipeline automation and orchestration")

print("\n" + "="*50)
print("🎉 DATA TRANSFORMATION PIPELINE COMPLETE!")
print("="*50)
```

    
    🎯 Next Steps for MLOps:
      1. Model training using transformed features
      2. Model validation and testing
      3. Model deployment and monitoring
      4. Data drift monitoring using quality metrics
      5. Pipeline automation and orchestration
    
    ==================================================
    🎉 DATA TRANSFORMATION PIPELINE COMPLETE!
    ==================================================

