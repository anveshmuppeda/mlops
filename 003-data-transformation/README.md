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
This will create a dataset `mock_data.csv` in the `data` directory.
Now deactivate the virtual environment:
```bash
deactivate
```

# now let's open the Jupyter Notebook:
```bash
jupyter notebook
```
# This will open the Jupyter Notebook in your default web browser.

Now you create a new notebook `data_transformation.ipynb` by clicking on the "New" button and selecting "Python 3" (or the version you have installed).
This will create a new notebook where you can write and execute Python code.
the default name for the notebook will be `Untitled.ipynb`, you can rename it to `data_transformation.ipynb` by clicking on the notebook name at the top of the page. or go to `File` -> `Rename` and enter the new name.




# The notebook includes the following steps:


## References
1. [Anaconda Installation](https://docs.anaconda.com/anaconda/install/)
2. [Jupyter Notebook Installation](https://jupyter.org/install)
3. [JupyterLab Installation](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html)
4. [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
5. [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
6. [Creating a Virtual Environment](https://docs.python.org/3/library/venv.html)
7. [Python Data Cleaning](https://realpython.com/python-data-cleaning-numpy-pandas/)
8. [Feature Engineering with Pandas](https://towardsdatascience.com/feature-engineering-with-pandas-3f8f8c1b2f3)
9. [Data Normalization Techniques](https://machinelearningmastery.com/data-normalization-with-python/)
10. [Data Transformation Techniques](https://towardsdatascience.com/data-transformation-techniques-in-machine-learning-3f8f8c1b2f3)
11. [Python Data Transformation](https://www.datacamp.com/community/tutorials/python-data-transformation)
12. [Data Transformation in Machine Learning](https://www.analyticsvidhya.com/blog/2020/04/data-transformation-in-machine-learning/)
13. [Data Transformation Techniques](https://www.geeksforgeeks.org/data-transformation-techniques/)
14. [Data Transformation in Python](https://www.datacamp.com/community/tutorials/data-transformation-in-python)
15. [Data Transformation with Pandas](https://www.datacamp.com/community/tutorials)



