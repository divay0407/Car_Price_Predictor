# 🚗 Car Price Prediction using Machine Learning

A machine learning project that predicts the selling price of a used car based on its specifications. This project demonstrates the complete data science workflow, from raw data preprocessing to model deployment-ready pipelines.

---

## 📌 Project Overview

The objective of this project is to build an accurate machine learning model capable of predicting car prices using historical vehicle data.

The project follows a structured end-to-end pipeline that includes:

- Data Collection
- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Categorical Data Encoding
- Machine Learning Pipeline Creation
- Model Training & Evaluation
- Car Price Prediction

---

## 📂 Project Workflow

### 1. Raw Data Collection
- Imported the raw Excel dataset.
- Loaded the data using **Pandas**.

### 2. Data Cleaning
Performed several preprocessing steps including:
- Handling missing values
- Removing duplicate records
- Correcting inconsistent values
- Converting data types
- Feature selection

### 3. Exploratory Data Analysis (EDA)
Analyzed the dataset to understand relationships between variables through:
- Summary statistics
- Distribution plots
- Correlation analysis
- Box plots
- Histograms
- Scatter plots
- Pair plots
- Outlier detection

### 4. Feature Engineering
- Created meaningful features
- Removed unnecessary columns
- Prepared features for model training

### 5. Categorical Encoding
Encoded categorical variables using suitable encoding techniques to make them compatible with machine learning algorithms.

### 6. Pipeline Creation
Built a Scikit-learn Pipeline that automates:
- Data preprocessing
- Feature transformation
- Encoding
- Model training

This ensures reproducibility and prevents data leakage.

### 7. Model Training
Trained the model using regression algorithms and evaluated performance using appropriate metrics.

### 8. Prediction
The trained model predicts the estimated selling price of a car based on user-provided features.

---

## 📊 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook

---

## 📁 Project Structure

```
Car-Price-Prediction/
│
├── data/
│   └── Car_Price_Data.xlsx
│
├── notebooks/
│   └── Car_Price_Prediction.ipynb
│
├── models/
│   └── pipeline.pkl
│
├── README.md
└── requirements.txt
```

---

## ⚙️ Machine Learning Workflow

```
Raw Excel Data
        │
        ▼
Data Cleaning
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Feature Engineering
        │
        ▼
Categorical Encoding
        │
        ▼
Scikit-learn Pipeline
        │
        ▼
Model Training
        │
        ▼
Model Evaluation
        │
        ▼
Car Price Prediction
```

---

## 📈 Model Evaluation

The model performance was evaluated using regression metrics such as:

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

---

## 🎯 Features

- End-to-end machine learning workflow
- Clean and organized preprocessing
- Exploratory Data Analysis with visualizations
- Automated preprocessing using Scikit-learn Pipeline
- Predicts used car selling prices
- Reproducible and scalable workflow

---

## 🚀 How to Run

### Clone the repository

```bash
git clone https://github.com/your-username/car-price-prediction.git
```

### Navigate to the project

```bash
cd car-price-prediction
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Launch Jupyter Notebook

```bash
jupyter notebook
```

Open the notebook and run all cells.

---


---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome. Feel free to fork this repository and submit a pull request.

---

## ⭐ If you found this project useful, don't forget to star the repository!
