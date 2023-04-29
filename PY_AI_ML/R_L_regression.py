from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = load_boston()
dataset = pd.DataFrame(df.data) #-- prints independent features

dataset.columns = df.feature_names #-- print feature names 

#print(df.target.shape) #-- prints shape of df

dataset["Price"] = df.target #-- add feature
#print(dataset.head()) #-- display

X = dataset.iloc[:,:-1] #-- independent features
y = dataset.iloc[:,-1]  #-- dependent features

#-- LINEAR REGRESSION --#

lin_regressor = LinearRegression()
mse = cross_val_score(lin_regressor,X,y,scoring = 'neg_mean_squared_error',cv=5)
mean_mse = np.mean(mse)
#print(mean_mse)

#-- RIDGE REGRESSION --#

ridge = Ridge()
parameters = {'alpha':[1e-15,1e-10,1e-8,1e-3,1e-2,1,5,10,20,30,35,40,45,50,55,100]}
ridge_regressor = GridSearchCV(ridge,parameters,scoring = 'neg_mean_squared_error',cv=5)
ridge_regressor.fit(X,y)

#print(ridge_regressor.best_params_)
#print(ridge_regressor.best_score_)

#-- LASSO REGRESSION --#

lasso = Lasso()
parameters = parameters = {'alpha':[1e-15,1e-10,1e-8,1e-3,1e-2,1,5,10,20,30,35,40,45,50,55,100]}
lasso_regressor = GridSearchCV(lasso,parameters,scoring = 'neg_mean_squared_error',cv=5)
lasso_regressor.fit(X,y)

#print(lasso_regressor.best_params_)
#print(lasso_regressor.best_score_)

#-- TRAIN/TEST --#

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
prediction_ridge = ridge_regressor.predict(X_test)
prediction_lasso = lasso_regressor.predict(X_test)

print(sns.distplot(y_test-prediction_ridge))
plt.show()
print(sns.distplot(y_test-prediction_lasso))
plt.show()