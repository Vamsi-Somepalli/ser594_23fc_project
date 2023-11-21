import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import r2_score, mean_squared_error

import wf_ml_prediction
import wf_ml_training

filepath = 'data_processed/preprocessed_crime_data.csv'
df = pd.read_csv(filepath)

df['Date'] = pd.to_datetime(df['Date'])


df['Year'] = df['Date'].dt.year
df['Week'] = df['Date'].dt.isocalendar().week

df_grouped = df.groupby(['Year', 'Week', 'Beat', 'District']).size().reset_index(name='Incident Count')


X = df_grouped[['Year', 'Week', 'Beat', 'District']]
Y = df_grouped['Incident Count']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

X_train.to_csv('data_processed/X_train.csv', index=False)
X_test.to_csv('data_processed/X_test.csv', index=False)
Y_train.to_csv('data_processed/Y_train.csv', index=False)
Y_test.to_csv('data_processed/Y_test.csv', index=False)

Linear_model_file=wf_ml_training.train_linear_regression(X_train,Y_train)
Linear_prediction=wf_ml_prediction.predict(Linear_model_file,X_test)

Ridge_model_file=wf_ml_training.train_ridge_regression(X_train,Y_train)
Ridge_prediction=wf_ml_prediction.predict(Ridge_model_file,X_test)

Lasso_model_file=wf_ml_training.train_lasso_regression(X_train,Y_train)
Lasso_prediction=wf_ml_prediction.predict(Lasso_model_file,X_test)

Random_forest_model_file=wf_ml_training.train_Random_forest(X_train,Y_train)
Random_forest_prediction=wf_ml_prediction.predict(Random_forest_model_file,X_test)

DecisionTree_model_file = wf_ml_training.train_decision_tree(X_train, Y_train)
DecisionTree_prediction = wf_ml_prediction.predict(DecisionTree_model_file, X_test)

knn_model_file = wf_ml_training.train_knn(X_train, Y_train, k=5)
knn_prediction = wf_ml_prediction.predict(knn_model_file, X_test)

mse_knn = mean_squared_error(Y_test, knn_prediction)
r2_knn = r2_score(Y_test, knn_prediction)

mse_linear = mean_squared_error(Y_test, Linear_prediction)
r2_linear=r2_score(Y_test, Linear_prediction)

mse_ridge = mean_squared_error(Y_test,Ridge_prediction)
r2_ridge = r2_score(Y_test, Ridge_prediction)

mse_lasso = mean_squared_error(Y_test,Lasso_prediction)
r2_lasso = r2_score(Y_test, Lasso_prediction)

mse_rf = mean_squared_error(Y_test,Random_forest_prediction)
r2_rf = r2_score(Y_test, Random_forest_prediction)

mse_dt = mean_squared_error(Y_test, DecisionTree_prediction)
r2_dt = r2_score(Y_test, DecisionTree_prediction)

with open('evaluation/summary.txt', 'w') as file:
    file.write("****************Linear Regression****************")
    file.write(f'\nMean Squated Error:{mse_linear}')
    file.write(f'\nR2 score:{r2_linear}')
    file.write("\n****************Ridge Regression****************")
    file.write(f'\nMean Squated Error:{mse_ridge}')
    file.write(f'\nR2 score:{r2_ridge}')
    file.write("\n****************Lasso Regression****************")
    file.write(f'\nMean Squated Error:{mse_lasso}')
    file.write(f'\nR2 score:{r2_lasso}')
    file.write("\n****************Random Forest****************")
    file.write(f'\nMean Squated Error:{mse_rf}')
    file.write(f'\nR2 score:{r2_rf}')
    file.write("\n****************Decision Tree****************")
    file.write(f'\nMean Squared Error: {mse_dt}')
    file.write(f'\nR2 score: {r2_dt}')
    file.write("\n****************k-NN****************")
    file.write(f'\nMean Squared Error:{mse_knn}')
    file.write(f'\nR2 score:{r2_knn}')