# Data Transformation using Amazon SageMaker Data Wrangler
*A hands-on guide to building a data transformation workflow using Amazon SageMaker Data Wrangler.*
![SageMaker Data Wrangler](./img/mlops-sagemaker-datawrangler.png)

This guide demonstrates how to perform data transformation using **Amazon SageMaker Data Wrangler**, following similar steps to the [previous module](./../003-data-transformation/data_transformation.ipynb), but using the Data Wrangler UI instead of Jupyter notebooks.

## ✅ Prerequisites
- AWS account with SageMaker access
- `mock_data.csv` (located in the `data` folder of this repo)
- An S3 bucket to store your data

## 🚀 Step-by-Step Instructions

### 1. Upload Data to S3
1. Go to the [AWS S3 Console](https://s3.console.aws.amazon.com/).
2. Choose or create a new S3 bucket.
3. Upload the `mock_data.csv` file into this bucket.
![S3 Upload](./img/s3.png)

### 2. Set Up SageMaker Studio Environment
1. Go to the [AWS SageMaker Console](https://console.aws.amazon.com/sagemaker/).
2. Navigate to **"Domains"** under **Admin configurations**.
3. Click **Create Domain**, use the default settings, and click **Create**.
    ![Create Domain](./img/01-domain.png)
4. After the domain is created, click on the domain name.
5. Go to **User Profiles**, create a new profile (if not already created).
6. From the user profile, click **Launch app > Studio**.
   ![Launch Studio](./img/02-domain.png)
   ![Studio Home](./img/03-studio.png)


### 3. Open Data Wrangler
1. In SageMaker Studio, on the left sidebar, click on the **Data** icon.
2. Select the **Data Wrangler** tab.
  ![Data Wrangler Tab](./img/04-data.png)
3. Click **Start Canvas**, then **Open in Canvas** to launch Data Wrangler.
  ![Data Wrangler Canvas](./img/05-canvas.png)

### 4. Import Dataset
1. Click **Import and prepare data**.
![Import Data](./img/06-dw.png)
2. Select **Dataset type** as **Tabular**.
3. Choose **S3** as your data source.
![Select S3](./img/07-dw-s3.png)
4. Locate and select the `mock_data.csv` file.
5. Click **Import** to load the dataset into Data Wrangler.
![Import Dataset](./img/08-dw-import.png)
![Data Wrangler Interface](./img/09-flow.png)
6. Rename the default flow if desired (from the top of the interface).
![Rename Flow](./img/10-rename.png)

### 5. Apply Data Cleaning & Transformation
Click **Transform** and apply the following steps:
![Transform Data](./img/11-new-task.png)

- ✅ **Remove duplicates**
  ![Remove Duplicates](./img/12-drop.png)
- ✅ **Handle missing values**:
  - Fill `age` with **mean**
    ![Fill Age Mean](./img/13-miss.png)
  - Fill `salary` with **median**
  - Fill `department` with **"Unknown"**
    ![Fill Department Unknown](./img/14-miss.png)
- ✅ **Parse `profile` column** into:
  - `address`, `phone`, `email`
    ![Parse Profile](./img/15-devide.png)
- ✅ **Rename** the extracted columns appropriately
  - Rename `profile.address` to `address`
  - Rename `profile.phone` to `phone`
  - Rename `profile.email` to `email`
    ![Rename Columns](./img/16-rename.png)
- ✅ **Drop the original `profile` column**
  ![Drop Profile Column](./img/17-drop.png)

> After each transformation, click **Apply** to save the change.

### 6. Export Cleaned Dataset
1. Click **Export** from the toolbar.
  ![Export Data](./img/21-export.png)
2. Select **Amazon S3** as the export destination.
3. Choose the output S3 bucket and specify a folder path.
  ![Export S3](./img/22-export-s3.png)
4. Click **Export**.

### 7. Feature Engineering
Use **Custom Formula Transformations** to add the following:

- ✅ **`address_length`**:
  ```sql
  IF(address IS NOT NULL, length(cast(address AS string)), 0)
  ```
  ![Address Length](./img/18-add.png)
- ✅ **`salary_category`**:
  ```sql
  CASE
      WHEN salary IS NULL THEN 'unknown'
      WHEN salary <= 50000 THEN 'low'
      WHEN salary > 50000 AND salary <= 70000 THEN 'medium'
      WHEN salary > 70000 AND salary <= 100000 THEN 'high'
      ELSE 'very high'
  END
  ```
  ![Salary Category](./img/20-salary.png)

- ✅ **`age_group`**:
  ```sql
  CASE
      WHEN age IS NULL THEN 'Unknown'
      WHEN age <= 25 THEN 'Young'
      WHEN age > 25 AND age <= 35 THEN 'Early Career'
      WHEN age > 35 AND age <= 45 THEN 'Mid Career'
      WHEN age > 45 AND age <= 55 THEN 'Senior'
      ELSE 'Experienced'
  END
  ```
  ![Age Group](./img/19-age.png)

> After each formula transformation, click **Apply**.

![Feature Engineering](./img/23-steps.png)

### 8. Export Final Dataset
1. Click **Export** again after feature engineering.
2. Choose the **same or a new S3 bucket**.
3. Provide an output path for the final transformed dataset.
4. Click **Export** to complete.

### 9. Final Output
- The final dataset will be available in the specified S3 bucket.
- You can access it via the S3 console or programmatically using AWS SDKs.
![Final Output](./img/24-fullflow.png)

## 🧹 Cleanup Resources
To avoid unwanted charges:

1. Delete the S3 bucket (if no longer needed).
2. In SageMaker Studio, go to **Data Wrangler > Canvas** and click **Stop**.
3. Delete the SageMaker **Domain** and **User Profile** (if unused).
4. Optionally, delete the entire **SageMaker Studio** environment.

## ✅ You’re Done!
You've successfully set up Amazon SageMaker Data Wrangler, transformed your dataset, performed feature engineering, and exported your final dataset for further use in ML pipelines or analysis.

## Next Steps
1. **Model Training**: Use transformed features for ML model development
2. **Model Validation**: Implement cross-validation and testing strategies
3. **Model Deployment**: Deploy trained models to production
4. **Data Drift Monitoring**: Monitor for changes in data distribution
5. **Pipeline Automation**: Implement automated pipeline orchestration
