#### SER594: Machine Learning Evaluation
#### Crime Prediction: Weekly Incident Forecasting Using Machine Learning Approach (title)
#### Vamsi Krishna Somepalli (author)
#### 11/20/2023 (date)

## Evaluation Metrics
### Metric 1
**Name:** Mean Squared Error

**Choice Justification:** MSE measures the average squared difference between predicted and actual values, focusing on the impact of larger errors and providing overall view on model accuracy.

**Interpretation:** If MSE is lower that indicated model has better accuracy

### Metric 2
**Name:** R square

**Choice Justification:** This metric is to evaluate the performance of regresion model. This measures the amount of variance in the predictions.It ranges from 0 to 1. 1 indicates perfect preciction.


## Alternative Models
### Alternative 1: Ridge regression
**Construction:** Ridge regression is a modified version of linear regression. this will adds a penalty for large coefficients, helping prevent overfitting of predictions mainly in presence of correlated predictions

**Evaluation:** Ridge regression shows similar performance to linear regression,with high MSE and very low R2 which shows this model is poor fit for the data (Linear models might not be a good fit for this data).

### Alternative 2: Decission Tree
**Construction:** Decision Trees are a versatile model for regression and classification. They recursively split the data based on feature conditions, forming a tree structure. Decision Trees can capture non-linear relationships and are less prone to overfitting

**Evaluation:** It performs better than linear models, there's room for improvement to reduce overfitting.

### Alternative 3: Random Forest
**Construction:** Random Forests use decision trees as base models,and when dealing with complex, non-linear relationships data and reduces overfitting through ensemble learning.

**Evaluation:** Random Forest outperforms above all linear models with significantly lower mean squared error and a high R2 score of about 0.6, demonstrating a strong fit to the data


## Best Model

**Model:** Random Forest