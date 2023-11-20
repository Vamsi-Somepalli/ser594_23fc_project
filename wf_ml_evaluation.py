import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

import wf_ml_prediction
import wf_ml_training

filepath='data_processed/preprocessed_crime_data.csv'
df=pd.read_csv(filepath)

df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)


monthly_data = df.resample('W').size()


df_monthly = pd.DataFrame({'YearWeek': monthly_data.index, 'Incident_Count': monthly_data.values})
df_monthly.set_index('YearWeek', inplace=True)


df_monthly['Numeric_YearWeek'] = range(1, len(df_monthly) + 1)

# print(df_monthly)

X = df_monthly[['Numeric_YearWeek']]
Y = df_monthly['Incident_Count']
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
Ransom_forest_prediction=wf_ml_prediction.predict(Random_forest_model_file,X_test)

mse_linear = mean_squared_error(Y_test, Linear_prediction)
mae_linear = mean_absolute_error(Y_test, Linear_prediction)

mse_ridge = mean_squared_error(Y_test,Ridge_prediction)
mae_ridge = mean_absolute_error(Y_test,Ridge_prediction)

mse_lasso = mean_squared_error(Y_test,Lasso_prediction)
mae_lasso = mean_absolute_error(Y_test,Lasso_prediction)

mse_rf = mean_squared_error(Y_test,Lasso_prediction)
mae_rf = mean_absolute_error(Y_test,Lasso_prediction)

with open('evaluation/summary.txt', 'w') as file:
    file.write("****************Linear Regression****************")
    file.write(f'\nMean Squated Error:{mse_linear}')
    file.write(f'\nMean Absolute Error: {mae_linear}')
    file.write("\n****************Ridge Regression****************")
    file.write(f'\nMean Squated Error:{mse_ridge}')
    file.write(f'\nMean Absolute Error: {mae_ridge}')
    file.write("\n****************Lasso Regression****************")
    file.write(f'\nMean Squated Error:{mse_lasso}')
    file.write(f'\nMean Absolute Error: {mae_lasso}')
    file.write("\n****************Random Forest****************")
    file.write(f'\nMean Squated Error:{mse_rf}')
    file.write(f'\nMean Absolute Error: {mae_rf}')