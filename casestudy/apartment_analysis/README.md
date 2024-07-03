# Casestudy: Scraping and Analyzing data found on Munich's subsection on wggesucht.de
## Introduction

In this casestudy, we will explore the process of scraping and analyzing data from Munich's subsection on wggesucht.de. This popular website is a valuable source of information for apartment listings in Munich. By leveraging web scraping techniques, we can gather data and gain insights into the rental market in the city.

## Objectives

The main objectives of this casestudy are:

1. Scrape apartment data from wggesucht.de using Python.
2. Clean and preprocess the scraped data.
3. Perform exploratory data analysis to gain insights into the rental market.
4. Visualize the data using various plotting libraries.
5. Extract meaningful conclusions and recommendations based on the analysis.

## Tools and Technologies

To accomplish our objectives, we will be using the following tools and technologies:

- Python: A versatile programming language for web scraping and data analysis.
- Beautiful Soup: A Python library for parsing HTML and XML documents.
- Pandas: A powerful data manipulation and analysis library.
- Matplotlib: A plotting library for creating visualizations.
- Jupyter Notebook: An interactive environment for data analysis and visualization.
- Some other libraries


In the upcoming sections, we will delve into the details of the web scraping script, the data cleaning script, and the regression analysis script. These sections will provide a step-by-step guide on how to extract data from wggesucht.de, clean and preprocess the scraped data, and perform regression analysis to gain insights into Munich's rental market.

# Web Scraping Script (scraper.py)

Import Libraries:
The script starts by importing necessary libraries for web scraping such as requests, BeautifulSoup, and pandas.

Define Scraper Function:
It defines a function to scrape data from a specified website. This function sends a request to the webpage, parses the HTML content using BeautifulSoup, and extracts relevant data.

Data Extraction and Storage:
Extracted data is stored in a pandas DataFrame. The script iterates over multiple pages or items to gather comprehensive data.

Save Data:
The scraped data is saved to a CSV file for further analysis.

These scripts collectively perform data cleaning, preparation, and regression analysis to derive meaningful insights from the dataset. The web scraping script supports the data acquisition process, ensuring that the analysis has the necessary data to begin with.


# Data Cleaning Script (clean_up_data.ipynb)

Import Necessary Libraries:
The script begins by importing essential libraries such as pandas, re, os, requests, shapely, geopy, ee, geemap, matplotlib, and numpy.

Load Data:
It loads the dataset (wggesucht_scraped_24_05.csv) into a DataFrame using pandas.

Initial Data Inspection:
The script displays the DataFrame to inspect its initial state.

Feature Engineering:
It creates new features by calculating the length of strings in the 'Title' and 'LookingFor' columns and storing these lengths in new columns ('Title_length' and 'LookingFor_length').

Data Cleaning:
- Removes non-numeric characters from the 'Size' column.
- Drops unnecessary columns ('Price', 'ExtraCosts', 'OtherCosts').
- Replaces 'n.a.' values in specified columns ('RedemptionAgreement', 'DateFreeTill') with 0.
- Removes the '€' symbol from the 'PriceTotal' and 'Deposit' columns.

Transform 'OnlineSince' Column:
The script defines a function to transform values in the 'OnlineSince' column from a string format to a numerical representation in hours, considering various formats (e.g., minutes, hours, days).

Geocoding Addresses:
It defines a function to retrieve coordinates for addresses using the Nominatim tool from the geopy library.

Display Cleaned Data:
The script displays the cleaned DataFrame for final inspection.

# Regression Analysis Script (regression_analysis.ipynb)

Import Libraries:
Imports necessary libraries such as pandas, seaborn, matplotlib, statsmodels, numpy, and scipy for data handling, visualization, and statistical analysis.

Load and Prepare Data:
- Loads the cleaned dataset from a CSV file.
- Displays the first few rows of the DataFrame for inspection.

Visualize Data:
Uses seaborn to create a pairplot to visualize relationships between variables.

Correlation Matrix:
Generates a heatmap to display the correlation matrix of the variables in the dataset.

Define Features and Target:
- Defines the independent variables (features) and the dependent variable (target) for the regression analysis.
- Splits the data into features (X) and target (y).

Add Constant and Fit Model:
- Adds a constant to the features and fits an ordinary least squares (OLS) regression model using statsmodels.

Model Summary:
Displays the summary of the regression model, including coefficients, p-values, R-squared value, and other statistics.

Residual Plots:
- Creates residual plots to assess the goodness of fit of the model.
- Plots residuals vs. fitted values and Q-Q plots to check the normality of residuals.

Model Diagnostics:
- Calculates and prints the mean of residuals to ensure they average to zero.
- Performs the Breusch-Pagan test for heteroscedasticity.
- Conducts the Durbin-Watson test for autocorrelation.
- Performs the Shapiro-Wilk test to check the normality of residuals.

Plot Residuals and Q-Q Plot:
- Visualizes the residuals to identify patterns.
- Creates Q-Q plots to assess if residuals follow a normal distribution.


This markdown file presents a casestudy on scraping and analyzing data from Munich's subsection on wggesucht.de. The objectives of the casestudy include scraping apartment data, cleaning and preprocessing the data, performing exploratory data analysis, visualizing the data, and extracting conclusions and recommendations. The tools and technologies used in this casestudy include Python, Beautiful Soup, Pandas, Matplotlib, and Jupyter Notebook.

The file includes scripts for web scraping, data cleaning, and regression analysis. The web scraping script imports necessary libraries, defines a scraper function, extracts and stores data in a DataFrame, and saves the data to a CSV file. The data cleaning script imports libraries, loads the dataset, performs initial data inspection, feature engineering, data cleaning, transforms the 'OnlineSince' column, geocodes addresses, and displays the cleaned data. The regression analysis script imports libraries, loads and prepares the data, visualizes the data, defines features and target, adds constant and fits a regression model, displays the model summary, creates residual plots, performs model diagnostics, and plots residuals and Q-Q plots.

Please note that the thought process of evaluating the regression analysis will be in a separate file. This markdown file focuses on the technical aspects of the casestudy.

