import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import ensemble
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import GridSearchCV

df = pd.read_csv('C:\\Users\\Devil\\Documents\\Test_Data\\Melbourne_housing_FULL.csv')
del df['Address']
del df['Method']
del df['SellerG']
del df['Date']
del df['Postcode']
del df['Lattitude']
del df['Longtitude']
del df['Regionname']
del df['Propertycount']
df.dropna(axis=0,how='any',thresh=None,subset=None,inplace=True)
df = pd.get_dummies(df,columns=['Suburb','CouncilArea','Type'])
X=df.drop('Price',axis = 1)
y = df['Price']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,shuffle=True)

model = ensemble.GradientBoostingRegressor()
hyperparameters={'n_estimators':[200,300],'learning_rate':[0.01,0.02],
'max_depth':[4,6],'min_samples_split':[3,4],'min_samples_leaf':[5,6],
'max_features':[0.8,0.9],'loss':['squared_error','lad','huber']}

grid = GridSearchCV(model,hyperparameters,n_jobs=4)
grid.fit(X_train, y_train)
grid.best_params_

mae_train = mean_absolute_error(y_train,model.predict(X_train))
print("Training Set Mean Absolute Error:%.2f"%mae_train)

mae_test = mean_absolute_error(y_test,model.predict(X_test))
print("Test Set Mean Absolute Error:%.2f"%mae_test)

