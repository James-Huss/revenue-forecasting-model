# Revenue Forecasting Model

## Overview
This project forecasts future revenue using time series and machine learning models — specifically **Prophet** and **XGBoost** — applied to sample Walmart sales data. The goal is to demonstrate practical data analytics skills including data cleaning, feature engineering, modeling, and visualization.

## Tools & Technologies
- Python (Pandas, Prophet, XGBoost, scikit-learn)
- Jupyter Notebooks
- Tableau Public (for dashboard visualizations)

## Dataset
This project uses the publicly available Walmart sales dataset from Kaggle:

[Walmart Sales Dataset by Mikhail1681](https://www.kaggle.com/datasets/mikhail1681/walmart-sales)

All data used is anonymized and sample-based for demonstration purposes.

## Key Features
- Data cleaning and preprocessing scripts to combine and prepare sales data for modeling
- Time series forecasting with Prophet to capture seasonality and trends
- Gradient boosting regression with XGBoost for predictive accuracy
- Model evaluation using MAE, RMSE, and MAPE metrics
- Visualization of forecasts and confidence intervals via Tableau dashboard

## Project Structure
revenue-forecasting-model/
├── README.md
├── data/ # Sample or anonymized Walmart sales data CSVs
├── notebooks/ # Jupyter notebooks/python scripts for cleaning, feature engineering, and modeling
├── dashboards/ # Tableau Public workbook (.twb)
└── images/ # Forecast plots, model evaluation charts, and dashboard screenshots

## How to Use
1. Clone the repository:
   git clone https://github.com/yourusername/revenue-forecasting-model.git
2. Install required Python libraries:
   pip install -r requirements.txt
3. Execute the forecasting notebooks to generate predictions and evaluation metrics
4. Run the combining scripts in order:
   Combining scripts in 'notebooks/'
5. Open the Tableau workbook in 'dashboards/' to explore the interactive dashboards or view screenshots in 'images/'

## Credits
- Dataset sourced from [Kaggle - Walmart Sales Dataset by Mikhail1681](https://www.kaggle.com/datasets/mikhail1681/walmart-sales)

---

Feel free to explore and reach out if you have any questions or suggestions!
