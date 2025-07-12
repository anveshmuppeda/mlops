# Data Transformation 
# This module is responsible for transforming raw data into a format suitable for training machine learning models.
# It includes data cleaning, normalization, and feature engineering steps.
 For this module we are using the `Anaconda` with `jupyter` notebook.  
# The data transformation process is defined in the `data_transformation.ipynb` notebook.

To install anaconda, you can use the following command:
```bash
brew install anaconda
```
After installing Anaconda, install jupyter CLI with the following command:
```bash
brew install jupyter
```

# This will install Jupyter Notebook, which is a web-based interactive computing environment.


# JupyterLab provides a more flexible and powerful interface for working with Jupyter Notebooks.

# You can choose either Jupyter Notebook or JupyterLab based on your preference.
# Once you have installed Jupyter
# After installing Anaconda, you can start Jupyter Notebook with the following command:
```bash
jupyter notebook
```

Now let's create the Dataset to perform the data transformation.
# create virtual environment
```bash
python3 -m venv data_transformation_env
```
# activate the virtual environment
```bash
source data_transformation_env/bin/activate
```
# install required packages
```bash
pip install pandas
```
# Create the data by running the following script:
```bash
python create_dataset.py
```
# This will create a dataset `mock_data.csv` in the `data` directory.

# now let's open the Jupyter Notebook:
```bash
jupyter notebook
```
# This will open the Jupyter Notebook in your default web browser.


# The notebook includes the following steps: