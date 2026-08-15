# TASK 2 - Titanic Exploratory Data Analysis

## Objective
Load a dataset, examine its features using descriptive statistics, identify trends and distributions, study relationships between variables, detect outliers and unusual patterns, and use summary statistics to answer business-style questions.

## Dataset
Titanic passenger dataset containing 891 records and 12 variables. The project uses the cleaned dataset produced in Task 1.

## Tools
- Python
- Pandas
- NumPy
- Matplotlib
- VS Code

## How to run
1. Open this folder in VS Code.
2. Open the terminal.
3. Install dependencies:
   `pip install -r requirements.txt`
4. Run:
   `python task2_eda.py`

## Main analysis
- Dataset structure and data types
- Descriptive statistics
- Categorical distributions
- Survival trends
- Relationships between passenger characteristics and survival
- Correlation analysis
- IQR-based outlier detection
- Business-style questions
- Automated charts and CSV outputs

## Output
All generated tables are stored in `output/`, and visualizations are stored in `output/charts/`.

## Important note
Outliers are identified for analytical investigation, not automatically removed. In the Titanic dataset, extreme fares or family-size values may represent legitimate observations.
