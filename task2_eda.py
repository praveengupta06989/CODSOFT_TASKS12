"""
TASK 2 - Exploratory Data Analysis (EDA)
Dataset: Titanic
Environment: VS Code / Python

This script:
1. Loads the cleaned Titanic dataset.
2. Examines structure and descriptive statistics.
3. Studies distributions and relationships.
4. Detects numerical outliers using IQR.
5. Answers business-style analytical questions.
6. Saves tables and charts into the output/ folder.
"""

from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "cleaned_titanic.csv"
OUTPUT_DIR = BASE_DIR / "output"
CHART_DIR = OUTPUT_DIR / "charts"
OUTPUT_DIR.mkdir(exist_ok=True)
CHART_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH)

print("=" * 70)
print("TASK 2 - TITANIC EXPLORATORY DATA ANALYSIS")
print("=" * 70)

print("\n1. DATASET OVERVIEW")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")
print("\nColumns and data types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isna().sum())

print("\n2. DESCRIPTIVE STATISTICS")
numeric_cols = ["Age", "Fare", "SibSp", "Parch", "Pclass"]
stats = df[numeric_cols].describe().T
stats["median"] = df[numeric_cols].median()
stats.to_csv(OUTPUT_DIR / "descriptive_statistics.csv")
print(stats)

print("\n3. DISTRIBUTIONS")
print("\nSex:")
print(df["Sex"].value_counts())
print("\nPassenger class:")
print(df["Pclass"].value_counts().sort_index())
print("\nEmbarked:")
print(df["Embarked"].value_counts())

print("\n4. OUTLIER DETECTION USING IQR")
outlier_results = []
for col in ["Age", "Fare", "SibSp", "Parch"]:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    mask = (df[col] < lower) | (df[col] > upper)

    outlier_results.append({
        "Variable": col,
        "Q1": q1,
        "Q3": q3,
        "IQR": iqr,
        "Lower_Bound": lower,
        "Upper_Bound": upper,
        "Outlier_Count": int(mask.sum()),
        "Outlier_Percentage": mask.mean() * 100
    })

outliers = pd.DataFrame(outlier_results)
outliers.to_csv(OUTPUT_DIR / "outlier_analysis.csv", index=False)
print(outliers.to_string(index=False))

print("\n5. RELATIONSHIPS WITH SURVIVAL")
survival_by_sex = df.groupby("Sex")["Survived"].mean().mul(100)
survival_by_class = df.groupby("Pclass")["Survived"].mean().mul(100)

print("\nSurvival rate by sex (%):")
print(survival_by_sex)
print("\nSurvival rate by class (%):")
print(survival_by_class)

corr_cols = ["Survived", "Pclass", "Age", "SibSp", "Parch", "Fare"]
corr = df[corr_cols].corr(numeric_only=True)
corr.to_csv(OUTPUT_DIR / "correlation_matrix.csv")

print("\nCorrelation with survival:")
print(corr["Survived"].sort_values(ascending=False))

print("\n6. BUSINESS-STYLE QUESTIONS")
print(f"Overall survival rate: {df['Survived'].mean() * 100:.2f}%")
print(f"Highest survival by sex: {survival_by_sex.idxmax()} ({survival_by_sex.max():.2f}%)")
print(f"Highest survival by class: Class {survival_by_class.idxmax()} ({survival_by_class.max():.2f}%)")
print(f"Lowest survival by class: Class {survival_by_class.idxmin()} ({survival_by_class.min():.2f}%)")

age_groups = pd.cut(
    df["Age"],
    bins=[0, 12, 18, 35, 60, 100],
    labels=["Child", "Teen", "Young Adult", "Adult", "Senior"],
    include_lowest=True
)
age_result = df.assign(AgeGroup=age_groups).groupby(
    "AgeGroup", observed=False
)["Survived"].mean().mul(100)

print("\nSurvival rate by age group (%):")
print(age_result)

print("\nEDA completed. Check the output/ folder for tables and charts.")
