import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.pandas.set_option('display.max_columns',None)
dataset = pd.read_csv('C:\\Users\\Devil\\Documents\\Test_Data\\train_hpart.csv')
#print(dset.shape)
#print(dset.head())

## Here we will check the percentage of nan values present in each feature
## 1 -step make the list of features which has missing values
features_with_na=[features for features in dataset.columns if dataset[features].isnull().sum()>1]
## 2- step print the feature name and the percentage of missing values

for feature in features_with_na:
    #print(feature, np.round(dataset[feature].isnull().mean(), 4),  ' % missing values')

    data = dataset.copy()

    # let's make a variable that indicates 1 if the observation was missing or zero otherwise
    data[feature] = np.where(data[feature].isnull(), 1, 0)
    
    # let's calculate the mean SalePrice where the information is missing or present
    data.groupby(feature)['SalePrice'].median().plot.bar()
    plt.title(feature)
    #plt.show()

#print("Id of Houses {}".format(len(dataset.Id)))

#- list of numerical variables
numerical_features = [feature for feature in dataset.columns if dataset[feature].dtypes != 'O']

#print('Number of numerical variables: ', len(numerical_features))

#-- visualise the numerical variables
#print(dataset[numerical_features].head())

# list of variables that contain year information
year_feature = [feature for feature in numerical_features if 'Yr' in feature or 'Year' in feature]
#print(year_feature)

#-- let's explore the content of these year variables
for feature in year_feature:
    #print(feature, dataset[feature].unique())

## Lets analyze the Temporal Datetime Variables
## We will check whether there is a relation between year the house is sold and the sales price

    dataset.groupby('YrSold')['SalePrice'].median().plot()
    plt.xlabel('Year Sold')
    plt.ylabel('Median House Price')
    plt.title("House Price vs YearSold")
    #plt.show()

## Here we will compare the difference between All years feature with SalePrice

for feature in year_feature:
    if feature!='YrSold':
        data=dataset.copy()
        ## We will capture the difference between year variable and year the house was sold for
        data[feature]=data['YrSold']-data[feature]

        plt.scatter(data[feature],data['SalePrice'])
        plt.xlabel(feature)
        plt.ylabel('SalePrice')
        #plt.show()

## Numerical variables are usually of 2 type
## 1. Continous variable and Discrete Variables

discrete_feature=[feature for feature in numerical_features if len(dataset[feature].unique())<25 and feature not in year_feature+['Id']]
#print("Discrete Variables Count: {}".format(len(discrete_feature)))

#print(discrete_feature)

#print(dataset[discrete_feature].head())

## Lets Find the realtionship between them and Sale PRice

for feature in discrete_feature:
    data=dataset.copy()
    data.groupby(feature)['SalePrice'].median().plot.bar()
    plt.xlabel(feature)
    plt.ylabel('SalePrice')
    plt.title(feature)
    #plt.show()

continuous_feature=[feature for feature in numerical_features if feature not in discrete_feature+year_feature+['Id']]
#print("Continuous feature Count {}".format(len(continuous_feature)))

## Lets analyse the continuous values by creating histograms to understand the distribution

for feature in continuous_feature:
    data=dataset.copy()
    data[feature].hist(bins=25)
    plt.xlabel(feature)
    plt.ylabel("Count")
    plt.title(feature)
    #plt.show()

## We will be using logarithmic transformation


for feature in continuous_feature:
    data=dataset.copy()
    if 0 in data[feature].unique():
        pass
    else:
        data[feature]=np.log(data[feature])
        data['SalePrice']=np.log(data['SalePrice'])
        plt.scatter(data[feature],data['SalePrice'])
        plt.xlabel(feature)
        plt.ylabel('SalesPrice')
        plt.title(feature)
        #plt.show()

for feature in continuous_feature:
    data=dataset.copy()
    if 0 in data[feature].unique():
        pass
    else:
        data[feature]=np.log(data[feature])
        data.boxplot(column=feature)
        plt.ylabel(feature)
        plt.title(feature)
        #plt.show()

categorical_features=[feature for feature in dataset.columns if data[feature].dtypes=='O']
#print(categorical_features)

#print(dataset[categorical_features].head())

#for feature in categorical_features:
    #print('The feature is {} and number of categories are {}'.format(feature,len(dataset[feature].unique())))

for feature in categorical_features:
    data=dataset.copy()
    data.groupby(feature)['SalePrice'].median().plot.bar()
    plt.xlabel(feature)
    plt.ylabel('SalePrice')
    plt.title(feature)
    #plt.show()