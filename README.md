
# 🔥 Calories Burnt Prediction Using Machine Learning

A machine learning project to predict calories burnt based on exercise-related data. This repository features full-cycle data preprocessing, model building, tuning, evaluation, and explainability using SHAP.

---

## 📌 Project Overview

This project aims to help users estimate the number of calories they burn during exercise based on biometric and activity inputs such as age, weight, heart rate, and workout duration.

---

## 📂 Dataset

- `exercise.csv`: Includes physiological and exercise session metrics.
- `calories.csv`: Contains the target variable — calories burnt.
- A synthetic dataset is also used for demonstration purposes.

---

## 🛠️ Features Used

- Age, Height, Weight
- Duration (Minutes)
- Heart Rate, Body Temperature
- Gender (One-hot encoded)
- **Engineered Features:**
  - BMI (Body Mass Index)
  - Age Binning (18–25, 26–35, etc.)

---

## 🤖 Models Implemented

| Model              | Type                 | Tuned?  |
|-------------------|----------------------|---------|
| XGBoost Regressor | Gradient Boosting    | ✅ Yes  |
| Random Forest     | Ensemble Learning    | ✅ No   |
| Ridge Regression  | Regularized Linear   | ✅ No   |

---

## 🎯 Hyperparameter Tuning

`GridSearchCV` is used to optimize XGBoost on:
- `n_estimators`
- `max_depth`
- `learning_rate`

---

## 📈 Visualizations

- Feature Distributions & Correlation Heatmap
- Model MAE Comparison Bar Chart
- SHAP Summary and Bar Plots for Explainability

---

## 🧠 Explainability with SHAP

We use SHAP to interpret model predictions by showing how much each feature contributes to the final output for each prediction.

---

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/yourusername/calories-burnt-prediction.git
cd calories-burnt-prediction

# Install dependencies
pip install -r requirements.txt

# Run the Python script
python calories_burnt_prediction.py
```

---

## 📊 Sample Output (MAE)

| Model             | MAE Estimate |
|------------------|--------------|
| XGBoost (Tuned)  | ~X.XX        |
| Random Forest    | ~Y.YY        |
| Ridge Regression | ~Z.ZZ        |

---

## 🗂️ Repository Structure

```
📦calories-burnt-prediction
 ┣ 📜calories_burnt_prediction.py
 ┣ 📊exercise.csv
 ┣ 📊calories.csv
 ┣ 📄README.md
 ┣ 📄requirements.txt
```

---

## 📌 Future Enhancements

- Deploy using Streamlit for user input
- Track calories over time with session history
- Save and export predictions
