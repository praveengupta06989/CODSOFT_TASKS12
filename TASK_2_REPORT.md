# TASK 2 - Exploratory Data Analysis Report

## 1. Objective
The objective of this project is to perform Exploratory Data Analysis (EDA) on the Titanic passenger dataset. The analysis examines descriptive statistics, distributions, trends, relationships, outliers, and unusual patterns. Summary statistics are then used to answer practical business-style questions.

## 2. Dataset Overview
The dataset contains **891 passenger records** and **12 variables**. The variables include passenger class, sex, age, family relationships, fare, cabin information, embarkation port, and survival outcome.

The cleaned dataset from Task 1 was used so that Task 2 focuses on analysis rather than repeating data-cleaning operations.

## 3. Descriptive Statistics
The average passenger age was **29.36 years**, with a median of **28.00 years**. The average fare was **32.20**, while the median fare was **14.45**.

The difference between the mean and median fare indicates a **right-skewed fare distribution**, with a relatively small number of passengers paying very high fares.

## 4. Trends and Distributions
- The dataset contains **577 male** and **314 female** passengers.
- Class 3 is the largest passenger class.
- Embarkation port **S** is the most common.
- Overall survival was **38.38%**.
- Fare values are strongly concentrated at the lower end, with a long upper tail.
- Passenger ages are concentrated around young-adult and adult ranges.

## 5. Relationships Between Variables
Survival varies substantially by sex and passenger class.

### Survival by Sex
- Female survival rate: **74.20%**
- Male survival rate: **18.89%**

This shows a major difference in survival outcomes between the two groups.

### Survival by Passenger Class
- Class 1: **62.96%**
- Class 2: **47.28%**
- Class 3: **24.24%**

The pattern shows that passenger class is strongly associated with survival.

## 6. Outlier Detection
The IQR method was applied to Age, Fare, SibSp, and Parch.

Variable  Outlier_Count  Outlier_Percentage
     Age             66                7.41
    Fare            116               13.02
   SibSp             46                5.16
   Parch            213               23.91

Outliers were **not automatically deleted** because extreme values can be genuine observations. For example, high fares may reflect premium tickets, while large SibSp/Parch values may represent passengers traveling with larger families.

## 7. Business-Style Questions and Answers

1. **What was the overall survival rate?**  
   **38.38%** of passengers survived.

2. **Which sex had the higher survival rate?**  
   **Female**, with a survival rate of **74.20%**.

3. **Which passenger class had the highest survival rate?**  
   **Class 1**, at **62.96%**.

4. **Which passenger class had the lowest survival rate?**  
   **Class 3**, at **24.24%**.

5. **Which numeric feature has the strongest absolute correlation with survival?**  
   **Pclass**, with correlation **-0.338**.

## 8. Key Findings
- Survival was not evenly distributed across passengers.
- Sex was a major differentiating factor in survival outcomes.
- Higher passenger class was associated with higher survival.
- Fare was positively associated with survival, although this relationship can partly reflect passenger class.
- Fare contained notable high-value outliers and a strongly right-skewed distribution.
- The analysis demonstrates why descriptive statistics and segmentation are useful before building predictive models.

## 9. Conclusion
The EDA reveals clear and meaningful patterns in the Titanic dataset. Survival was strongly associated with passenger characteristics, especially sex and passenger class. Distribution analysis also identified skewness in fare values and outliers that should be investigated rather than blindly removed. The resulting statistics and visualizations provide a strong analytical foundation for further statistical or machine-learning work.

## 10. Deliverables
- `task2_eda.py` - complete VS Code Python analysis
- `cleaned_titanic.csv` - Task 1 cleaned dataset used for analysis
- `output/descriptive_statistics.csv`
- `output/categorical_summary.csv`
- `output/outlier_analysis.csv`
- `output/correlation_matrix.csv`
- `output/business_questions_answers.csv`
- `output/charts/` - visualization set
