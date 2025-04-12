# -*- coding: utf-8 -*-
"""CALORIES BURNT PREDICTION.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Z8Bz4EdQq2MG_XnZB0rXmB_MBmtLQZSB

IMPORTING THE IMPORTANT LIBRARIES
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn import metrics

"""DATA COLOLECTION AND PRE-PROCESSING"""

calories = pd.read_csv('/content/calories.csv')
exercise_data = pd.read_csv('/content/exercise.csv')

calories.head()

exercise_data.head()

"""COMBINING THE 2 DATA FRAMES"""

calories_data = pd.concat([exercise_data, calories['Calories']], axis=1)

calories_data.head()

calories_data.shape

calories_data.info()

# checking for missing values
calories_data.isnull().sum()

calories_data.describe()

"""VISUALIZING THE DATA"""

sns.set()

# plotting the gender column in count plot
sns.countplot(calories_data['Gender'])

# finding the distribution of "Age" column
sns.distplot(calories_data['Age'])

# finding the distribution of "Height" column
sns.distplot(calories_data['Height'])

# finding the distribution of "Weight" column
sns.distplot(calories_data['Weight'])

# Convert 'Gender' column to numerical representation using one-hot encoding
calories_data = pd.get_dummies(calories_data, columns=['Gender'], drop_first=True)
correlation = calories_data.corr()

# constructing a heatmap to understand the correlation

plt.figure(figsize=(10,10))
sns.heatmap(correlation, cbar=True, square=True, fmt='.1f', annot=True, annot_kws={'size':8}, cmap='Blues')

"""CONVERTING TEXT TO NUMERICAL VALUE"""

calories_data.replace({"Gender":{'male':0,'female':1}}, inplace=True)

calories_data.head()

"""SEPARATING FEATURES AND TARGETS"""

X = calories_data.drop(columns=['User_ID','Calories'], axis=1)
Y = calories_data['Calories']

print(X)

print(Y)

"""SPLITTING DATA INTO TRAINING AND TEST DATA"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

"""TRAINING THE MODEL"""

# loading the model
model = XGBRegressor()

# training the model with X_train
model.fit(X_train, Y_train)

"""EVALUATING THE MODEL AND ITS PERFORMANCE"""

test_data_prediction = model.predict(X_test)
print(test_data_prediction)

# calculating mean absolute error
mae = metrics.mean_absolute_error(Y_test, test_data_prediction)

print("Mean Absolute Error = ", mae)

# Enhanced Calories Burnt Prediction Project

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error
import shap

# Simulate a dataset (replace with your actual dataset)
np.random.seed(42)
data = pd.DataFrame({
    'User_ID': np.arange(1, 1001),
    'Gender': np.random.choice(['male', 'female'], 1000),
    'Age': np.random.randint(18, 60, 1000),
    'Height': np.random.normal(165, 10, 1000),
    'Weight': np.random.normal(70, 15, 1000),
    'Duration': np.random.randint(10, 60, 1000),
    'Heart_Rate': np.random.randint(80, 160, 1000),
    'Body_Temp': np.random.normal(98.6, 0.7, 1000),
    'Calories': np.random.normal(300, 50, 1000)
})

# One-hot encode gender
data = pd.get_dummies(data, columns=['Gender'], drop_first=True)

# Feature Engineering
data['BMI'] = data['Weight'] / ((data['Height']/100)**2)
data['Age_Group'] = pd.cut(data['Age'], bins=[17, 25, 35, 45, 60], labels=['18-25', '26-35', '36-45', '46-60'])
data = pd.get_dummies(data, columns=['Age_Group'], drop_first=True)

# Define features and target
X = data.drop(columns=['User_ID', 'Calories'])
Y = data['Calories']

# Train-test split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

# Hyperparameter Tuning for XGBoost
xgb_model = XGBRegressor()
params = {
    'n_estimators': [50, 100, 150],
    'max_depth': [3, 5, 7],
    'learning_rate': [0.01, 0.1, 0.2]
}
grid = GridSearchCV(xgb_model, params, cv=3, scoring='neg_mean_absolute_error')
grid.fit(X_train, Y_train)

best_xgb_model = grid.best_estimator_

# Evaluate tuned model
xgb_predictions = best_xgb_model.predict(X_test)
xgb_mae = mean_absolute_error(Y_test, xgb_predictions)

print("Tuned XGBoost MAE:", xgb_mae)

# SHAP Explainability
explainer = shap.Explainer(best_xgb_model)
shap_values = explainer(X_test)

# SHAP Summary Plot
shap.summary_plot(shap_values, X_test, plot_type="bar", show=True)
shap.summary_plot(shap_values, X_test, show=True)

# Model comparison
models = {
    "XGBoost (Tuned)": best_xgb_model,
    "RandomForest": RandomForestRegressor(),
    "Ridge": Ridge()
}

# Train and evaluate remaining models
results = {"XGBoost (Tuned)": xgb_mae}
for name, model in models.items():
    if name != "XGBoost (Tuned)":
        model.fit(X_train, Y_train)
        predictions = model.predict(X_test)
        mae = mean_absolute_error(Y_test, predictions)
        results[name] = mae

# Model comparison plot
plt.figure(figsize=(8, 5))
sns.barplot(x=list(results.keys()), y=list(results.values()), palette='coolwarm')
plt.title("Model Comparison (Lower MAE is Better)")
plt.ylabel("Mean Absolute Error")
plt.xlabel("Model")
plt.grid(True)
plt.tight_layout()
plt.show()