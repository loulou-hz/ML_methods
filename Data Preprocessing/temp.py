# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Data Preporcessing
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

#Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:,: -1].values
y = dataset.iloc[:,: 3].values

from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values="NaN",strategy="mean",axis=0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3]= imputer.transform(X[:, 1:3])



