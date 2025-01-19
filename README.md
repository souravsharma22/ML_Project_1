# FWI Prediction from Algerian Fire Data

## Overview
This repository contains an end-to-end machine learning project for predicting the Fire Weather Index (FWI) using Algerian fire dataset. The project includes data exploration, feature selection and extraction, and model training with multiple regression techniques. Additionally, it features a web application built with the Flask framework for user interaction and deployment.

## Project Features

### Key Components
1. **Data Exploration and Visualization**
   - Comprehensive exploratory data analysis (EDA) to understand the dataset.
   - Feature selection and extraction to optimize model performance.
   - Visualization of key trends and relationships in the data.

2. **Machine Learning Models**
   - Implementation of various regression models:
     - Linear Regression
     - Ridge Regression
     - Lasso Regression
     - Elastic Net
     - LassoCV
     - RidgeCV
   - Comparison and selection of the best-performing model based on metrics such as RMSE and R².

3. **Web Application**
   - A user-friendly web app built with Flask, allowing users to input data and obtain FWI predictions.
   - The `application.py` file serves as the entry point for the Flask app.

4. **Deployment**
   - Configurations for deploying the application on AWS Elastic Beanstalk using `.ebextensions`.

## Getting Started

### Prerequisites
To run this project, you need:
- Python (>=3.8)
- Required libraries: `flask`, `numpy`, `pandas`, `scikit-learn`, `matplotlib`, `seaborn`
- AWS Elastic Beanstalk CLI (optional for deployment)

Install the required libraries using:
```bash
pip install -r requirements.txt
```

### Dataset
The Algerian fire dataset must be available locally in a CSV format. Place it in the `data/` directory and ensure it is properly preprocessed for analysis and modeling.

### Running the Project

#### Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/souravsharma22/ML_Project_1.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ML_Project_1
   ```
3. Run the Flask application:
   ```bash
   python application.py
   ```
4. Access the web app at `http://127.0.0.1:5000/` in your browser.

#### Deploying to AWS Elastic Beanstalk
1. Ensure your `.ebextensions` directory contains the necessary configuration files.
2. Initialize Elastic Beanstalk:
   ```bash
   eb init
   ```
3. Deploy the application:
   ```bash
   eb deploy
   ```

## Results
- Detailed EDA and visualizations are stored in the `notebooks/` directory.
- Model performance metrics and comparison are included in the `results/` directory.
- The Flask app enables real-time predictions based on user input.

## Future Scope
- Incorporate advanced regression models and hyperparameter tuning.
- Enhance the Flask app's UI/UX.
- Extend deployment to additional platforms such as Docker or Kubernetes.

## Contributions
Contributions are welcome! Feel free to open an issue or submit a pull request with suggestions or improvements.

## Contributor
Sourav Sharma
(souravbgp2210@gmail.com)
---


