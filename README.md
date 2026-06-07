\# 🚗 Bay Area Used Vehicle Market Analysis



Author: Alejandro Alvarez



\## 📊 Project Overview



This project analyzes approximately 16,000 used vehicle listings collected from Craigslist in the San Francisco Bay Area.



The goal is to understand how vehicle characteristics such as mileage, model year, and manufacturer influence vehicle prices using statistical and machine learning techniques.



\---



\## Version 1: Exploratory Data Analysis (EDA)



Features:



\- Data collection and cleaning

\- Vehicle price distributions

\- Mileage analysis

\- Manufacturer comparisons

\- Multiple regression modeling



📄 Report:

\[Version 1 Analysis](version\_1.html)



\---



\## Version 2: Vehicle Valuation Dashboard



Features:



\- Actual vs Predicted vehicle prices

\- Market valuation comparisons

\- Underpriced and overpriced vehicle identification

\- Searchable interactive table



📄 Report:

\[Version 2 Dashboard](Version-2.html)



\---



\## Version 3: Interactive Vehicle Price Estimator



Features:



\- User enters:

&#x20; - Vehicle Make

&#x20; - Model Year

&#x20; - Mileage



Models:



\- Multiple Regression

\- Random Forest

\- XGBoost



Output:



\- Estimated Market Value

\- Prediction Range

\- Individual Model Predictions



⚠️ Interactive version requires Shiny and is not hosted on GitHub Pages.



Source Code:



\[Version 3 Shiny App](Version\_3\_Shiny\_Estimator.Rmd)



\---



\## 🛠 Tools Used



\- R

\- tidyverse

\- ggplot2

\- randomForest

\- xgboost

\- DT

\- R Markdown

\- Git

\- GitHub Pages



\---



\## 📈 Key Results



\- 16,000 raw listings collected

\- 15,280 cleaned observations

\- 14,320 modeling observations

\- Random Forest explained approximately 90% of price variation

\- Mileage and vehicle age were the strongest predictors of vehicle value



\---



\## 📂 Repository Structure



```text

data/

scripts/

version\_1.Rmd

version\_1.html

Version 2.Rmd

Version-2.html

Version\_3\_Shiny\_Estimator.Rmd

README.md

