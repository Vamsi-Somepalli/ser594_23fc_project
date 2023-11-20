import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.ensemble import RandomForestRegressor

import pickle

# Load training and test dat
def train_linear_regression(X_train,Y_train):
    model = LinearRegression()
    model.fit(X_train, Y_train)
    Linear_model_file='models/linear_regression_model.pkl'
    with open(Linear_model_file, 'wb') as model_file:
        pickle.dump(model, model_file)
    return Linear_model_file
def train_ridge_regression(X_train,Y_train,alpha=0.1):
    model=Ridge(alpha=alpha)
    model.fit(X_train, Y_train)
    Ridge_model_file='models/ridge_regression_model.pkl'
    with open(Ridge_model_file, 'wb') as model_file:
        pickle.dump(model, model_file)
    return Ridge_model_file
def train_lasso_regression(X_train,Y_train,alpha=0.1):
    model=Lasso(alpha=alpha)
    model.fit(X_train, Y_train)
    Lasso_model_file='models/lasso_regression_model.pkl'
    with open(Lasso_model_file, 'wb') as model_file:
        pickle.dump(model, model_file)
    return Lasso_model_file
def train_Random_forest(X_train,Y_train):
    model=RandomForestRegressor()
    model.fit(X_train, Y_train)
    Rf_model_file='models/random_forest_model.pkl'
    with open(Rf_model_file, 'wb') as model_file:
        pickle.dump(model, model_file)
    return Rf_model_file



