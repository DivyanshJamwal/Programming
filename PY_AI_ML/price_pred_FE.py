from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.pandas.set_option('display.max_columns', None)
dataset = pd.read_csv('C:\\Users\\Devil\\Documents\\Test_Data\\train_hpart.csv')
#print(dataset.head())

## Always remember there way always be a chance of data leakage so we need to split the data first and then apply feature
## Engineering
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(dataset,dataset['SalePrice'],test_size=0.1,random_state=0)
#print(X_train.shape, X_test.shape)

## Let us capture all the nan values
## First lets handle Categorical features which are missing
features_nan=[feature for feature in dataset.columns if dataset[feature].isnull().sum()>1 and dataset[feature].dtypes=='O']

#for feature in features_nan:
    #print("{}: {}% missing values".format(feature,np.round(dataset[feature].isnull().mean(),4)))

## Replace missing value with a new label
def replace_cat_feature(dataset,features_nan):
    data=dataset.copy()
    data[features_nan]=data[features_nan].fillna('Missing')
    return data

dataset=replace_cat_feature(dataset,features_nan)

dataset[features_nan].isnull().sum()

#print(dataset.head())

## Now lets check for numerical variables the contains missing values
numerical_with_nan=[feature for feature in dataset.columns if dataset[feature].isnull().sum()>1 and dataset[feature].dtypes!='O']

## We will print the numerical nan variables and percentage of missing values

#for feature in numerical_with_nan:
    #print("{}: {}% missing value".format(feature,np.around(dataset[feature].isnull().mean(),4)))

## Replacing the numerical Missing Values

for feature in numerical_with_nan:
    ## We will replace by using median since there are outliers
    median_value=dataset[feature].median()
    
    ## create a new feature to capture nan values
    dataset[feature+'nan']=np.where(dataset[feature].isnull(),1,0)
    dataset[feature].fillna(median_value,inplace=True)
    
#print(dataset[numerical_with_nan].isnull().sum())

## Temporal Variables (Date Time Variables)

for feature in ['YearBuilt','YearRemodAdd','GarageYrBlt']:
    dataset[feature]=dataset['YrSold']-dataset[feature]

#print(dataset.head())

#print(dataset[['YearBuilt','YearRemodAdd','GarageYrBlt']].head())

num_features=['LotFrontage', 'LotArea', '1stFlrSF', 'GrLivArea', 'SalePrice']

for feature in num_features:
    dataset[feature]=np.log(dataset[feature])

categorical_features=[feature for feature in dataset.columns if dataset[feature].dtype=='O']
#print(categorical_features)

for feature in categorical_features:
    temp=dataset.groupby(feature)['SalePrice'].count()/len(dataset)
    temp_df=temp[temp>0.01].index
    dataset[feature]=np.where(dataset[feature].isin(temp_df),dataset[feature],'Rare_var')
    
#print(dataset.head(100))

for feature in categorical_features:
    labels_ordered=dataset.groupby([feature])['SalePrice'].mean().sort_values().index
    labels_ordered={k:i for i,k in enumerate(labels_ordered,0)}
    dataset[feature]=dataset[feature].map(labels_ordered)
#print(dataset.head(10))

scaling_feature=[feature for feature in dataset.columns if feature not in ['Id','SalePerice'] ]
#print(len(scaling_feature))

#print(scaling_feature)

#-- Feature Scale
feature_scale=[feature for feature in dataset.columns if feature not in ['Id','SalePrice']]

scaler=MinMaxScaler()
print(scaler.fit(dataset[feature_scale]))
