import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,SGDRegressor
from sklearn.ensemble import RandomForestRegressor,ExtraTreesRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
data= pd.read_csv("AirQualityUCI.csv")
data = data.drop(["Date", "Time","Unnamed: 15","Unnamed: 16" ], axis=1)
data = data.dropna()
data[data < 0] = np.nan
column_means = data.mean()
data = data.fillna(column_means)
x = data.drop(['RH'],axis= 1)
y = data["RH"]
x_data = np.array(x)
y_data = np.array(y)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, shuffle=True)
x_data= np.array(x_train)
y_data =  np.array(y_train)


def predictor(parameters):    
    model = ExtraTreesRegressor()
    model.fit(x_data,y_data)
    result = model.predict(parameters)
    return result[0]
    
    
    
