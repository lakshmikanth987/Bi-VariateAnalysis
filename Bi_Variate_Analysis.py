# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 19:51:19 2020

@author: Lakshmikanth

Title: Bi-Variate Analysis
"""
# Importing required libraries
import pandas as pd

#Imorting the csv file
data_retirval = pd.read_csv(r"*****\vgsales.csv", encoding='latin-1')

print(data_retirval.head(10))

# Scatter points
data_retirval.plot.scatter(x='Global_Sales', y ='Other_Sales')

# Hexplot
data_retirval.plot.hexbin(x='Global_Sales', y ='Other_Sales' , gridsize =15)

# Stacked plots
data_retirval.plot.bar(stacked=True)