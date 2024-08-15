## @Team: update this file as you see fit for our particular project.

# Proposal: Titanic Survivor Analysis Using Machine Learning

## Project Overview

The project aims to train a machine learning model to predict the survival of Titanic passengers based on passenger information. The analysis involves a detailed exploration of passenger data, feature engineering, and modeling to improve prediction accuracy. Additionally, we will incorporate a database component using SQLite to store processed data after feature engineering and reload it before proceeding with the machine learning steps.

## Project Team

The team of data scientists working on this project includes:

* Alexander F
* Kevin L
* Elias C
* Zhi L

The proposal outlines the goals, methodologies, deliverables, and tools that will support the successful completion of the Titanic Survivor Analysis.

## Key Tasks and Components

### Goals

1. **Data Exploration and Preprocessing:** Analyze the dataset to understand key features, handle missing data, and create new variables that may influence survival prediction.

2. **Hypothesis Development:** Establish hypotheses based on historical understanding of survival rates, particularly relating to demographic factors such as age, gender, and socioeconomic status.

3. **Model Development and Evaluation:** Train and evaluate multiple machine learning models, selecting the best-performing one based on validation accuracy.

4. **Insights and Reporting:** Provide insights on which factors played a significant role in survival predictions and generate reports on the models used and their accuracy.

### Procedure

1. **Data Exploration**

   * Load data from CSV files and understand the structure of the dataset.
   * Handle missing values and explore key variables.

2. **Feature Engineering**

   * Create new features from the existing dataset (e.g., extracting titles, creating family size, etc.).
   * Process the data into a format suitable for machine learning.

3. **SQLite Integration**

   * After feature engineering, store the processed data in a SQLite database.
   * Use SQLite to store only the necessary features for the remaining machine learning steps.

4. **Machine Learning & Model Selection**

   * Load the processed data from the SQLite database.
   * Split the data into training and validation sets, train different models, and compare their performance.   
   * Choose the best model based on accuracy.

5. **Model Prediction** 

   * Generate predictions on the test data using the selected model.

## Conclusion

This project leverages machine learning to predict Titanic passenger survival and provides valuable insights into historical and socio-economic factors. By comparing multiple models and selecting the best approach, we aim to develop a robust model with high predictive accuracy while uncovering human-interest stories embedded within the data.

---

## Data, Tools, Techniques, and Challenges

### Dataset Description

The dataset used in this project comes from Kaggle’s Titanic competition, which is publicly available for training machine learning models. The dataset contains 1309 entries split into training (891 records) and test sets (418 records). Each entry includes the following key features:

* **PassengerId:** Unique ID for each passenger.
* **Survived:** Survival (1) or non-survival (0) of the passenger.
* **Pclass:** Ticket class (1 = first, 2 = second, 3 = third).
* **Name:** Full name of the passenger.
* **Sex:** Gender of the passenger.
* **Age:** Age of the passenger.
* **SibSp:** Number of siblings/spouses aboard.
* **Parch:** Number of parents/children aboard.
* **Ticket:** Ticket number.
* **Fare:** Ticket price.
* **Cabin:** Cabin number.
* **Embarked:** Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton).

### Tools and Technologies

* Programming Language: Python 3.9+

* Libraries:

  * Data Processing: Pandas, NumPy
  * Visualization: Matplotlib, Seaborn
  * Machine Learning: Scikit-learn, XGBoost

* Software:

  * Jupyter Notebook for exploratory analysis and modeling.
  * Kaggle for dataset and competition submission.

### Potential Challenges

1. **Imbalanced Data:** Since the dataset contains more non-survivors than survivors, class imbalance may bias the models. We plan to address this by using balanced accuracy or precision-recall metrics.

2. **Feature Selection:** Identifying the most important features, particularly dealing with the non-numerical features such as Name, Ticket, and Cabin, requires careful attention.
Overfitting: Monitoring for overfitting using techniques like cross-validation and hyperparameter tuning to ensure the model generalizes well.

### Expected Outcomes

1. **Prediction Accuracy:** Achieve a prediction accuracy of 80% or higher on the test set.

2. **Insights into Factors Influencing Survival:** Provide detailed insights into the key factors influencing survival and their importance.
