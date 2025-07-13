# Data Transformation using Amazon SageMaker Data Wrangler

First let's set up the sagemaker data wrangler environment. This will allow us to use the data wrangler to transform the data.

1. Upload the `mock_data.csv` file to an S3 bucket. This file contains the original dataset that we will be transforming. (you can find the file in the `data` folder of this repository)

1. Access Amazon SageMaker AI from the AWS Management Console.
2. Navigate to the Add Configuration section.
3. Select Domains and then Create Domain.
4. Choose the default settings for the domain and click Create Domain.
5. Once the domain is created, click on the domain name to access it.
6. In the domain, navigate to user profiles and create a new user profile (if not already created).
7. From the user profile, click on the Launch app button and select Studio. This will open the SageMaker Studio environment.
8. From the SageMaker Studio environment, go to the left sidebar and click on the Data > Data Wrangler tab.
9. Start the Canvas by clicking on the Start Canvas button.
10. Once the Canvas is started, click on Open in Canvas to open the Data Wrangler interface.
11. In the Data Wrangler interface, click on the Import and prepare data button. Then select Dataset type (tabular or image).
12. Choose the data source (e.g., S3 bucket) and select the dataset you want to transform.
13. After selecting the dataset, click on the Import button to load the data into Data Wrangler.
14. Now it will create a new flow in Data Wrangler with the imported dataset.
15. You can rename the flow from the "Data Wrangler" tab by clicking on the flow name and entering a new name.
16. To transform the data, click on the Transform button in the Data Wrangler interface.
17. In the Transform section, you can apply various transformations to the dataset, such as filtering, aggregating, or joining data.
18. So in our case, we will apply the following cleaning and transformation steps:
    - Remove duplicate rows
    - Fill missing values in the "age" column with the mean value
    - Fill missing values in the "salary" column with the median value
    - Fill missing values in the "department" column with a default value of "Unknown"
    - Parse the "profile" column to extract address, phone, and email into separate columns.
    - Rename the newly extracted columns to "address", "phone", and "email"
    - Drop the "profile" column after extraction
19. After applying the transformations, click on the Apply button to save the changes to the dataset.
20. Now export the cleaned dataset to an S3 bucket by clicking on the Export button in the Data Wrangler interface.
21. Now perform the following feature engineering steps:
    - Create a new column "address_length" that contains the length of the "address" column
      * for this, I used custom formula transformation in Data Wrangler
      ```sql
      IF(address IS NOT NULL, length(cast(address AS string)), 0)
    ```
    - Create a new column "salary_category" based on the "salary" column (e.g., low, medium, high)
        * for this, I used custom formula transformation in Data Wrangler
        ```sql
        CASE
            WHEN salary IS NULL THEN 'unknown'
            WHEN salary <= 50000 THEN 'low'
            WHEN salary > 50000 AND salary <= 70000 THEN 'medium'
            WHEN salary > 70000 AND salary <= 100000 THEN 'high'
            ELSE 'very high'
        END
        ```
    - Create a new column "age_group" based on the "age" column
        * for this, I used custom formula transformation in Data Wrangler
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
22. After applying the feature engineering steps, click on the Apply button to save the changes to the dataset.
23. Finally, export the transformed dataset to an S3 bucket by clicking on the Export button in the Data Wrangler interface.
24. Choose the S3 bucket and specify the output path for the transformed dataset.
25. Click on the Export button to save the transformed dataset to the specified S3 bucket.

So these are the simple steps to set up the SageMaker Data Wrangler environment and perform data transformation using it.

That's it! You have successfully set up the SageMaker Data Wrangler environment and performed data transformation using it. You can now use the transformed dataset for further analysis or machine learning tasks.

## Cleanup
To clean up the resources created during this process, you can follow these steps:
1. Delete the S3 bucket where the transformed dataset is stored.
2. Stop the Data Wrangler > Canvas to release any resources being used.
3. Delete the SageMaker Domain and User Profile if they are no longer needed.
4. Optionally, delete the SageMaker Studio environment if it is not required for other tasks.
This will help you avoid unnecessary charges and keep your AWS account organized.
