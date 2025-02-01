# Predict the S&P index price

This project involves analyzing historical S&P 500 data, performing data cleaning, and applying analysis and modeling.


## Python version


## Project Files

### `dashboard.py`
This Python file contains a Streamlit dashboard that allows users to interact with the data.

### `requirements.txt`
This file contains a list of all Python dependencies required to run the project.

### `scrap.py`
This script handles web scraping to collect financial data (S&P 500).

### `sp500.ipynb`
This Jupyter Notebook contains the entire data cleaning, analysis, and modeling process.

## Project Setup and Installation


1. **Clone the repository** 

   ```
   git clone <repository_url>
   cd <repository_folder>
    ```
2. **Activate environment and install dependencies** 
   ```
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. **Run notebook** 
    ```
    jupyter notebook sp500.ipynb
    ```

4. **Run dashboard** 
   ```
    streamlit run dashboard.py
    ```
