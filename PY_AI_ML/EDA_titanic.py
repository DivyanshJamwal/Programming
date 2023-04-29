import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score


def impute_age(cols):
    Age = cols[0]
    Pclass = cols[1]

    if pd.isnull(Age):
        if Pclass == 1:
            return 37

        elif Pclass == 2:
            return 29

        else:
            return 24

    else:
        return Age

train = pd.read_csv('C:/Users/Devil/Documents/Test_Data/titanic_train.csv')
#print(train.head()) 
#print(train.isnull()) #-- shows null values
#print(sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')) #-- heatmap_null
sns.set_style('whitegrid')
#print(sns.countplot(x='Survived',hue='Sex',data=train,palette='rainbow'))
#print(sns.countplot(x='Survived',hue='Pclass',data=train,palette='rainbow'))
#print(sns.displot(train['Age'].dropna(),kde=False,bins=40))
#print(sns.countplot(x='SibSp',data=train))
#print(sns.displot(train['Fare'],kde=False,bins=30))
#print(sns.boxplot(x='Pclass',y='Age',data=train))
plt.show()

train['Age'] = train[['Age','Pclass']].apply(impute_age,axis=1)
train.drop('Cabin',axis=1,inplace=True)
train.dropna(axis=0,how='any',thresh=None,subset=None,inplace=True)

#print(sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis'))
plt.show()

embark = pd.get_dummies(train['Embarked'],drop_first=True)
sex = pd.get_dummies(train['Sex'],drop_first=True)

train.drop(['Embarked','Sex','Name','Ticket'],axis=1,inplace=True)
train = pd.concat([train,sex,embark],axis=1)
#print(train.head())

print(train.drop('Survived',axis=1).head())

print(train['Survived'].head())

X_train,X_test,y_train,y_test = train_test_split(train.drop('Survived',axis=1),train['Survived'],
test_size=0.30,random_state=101)

model = LogisticRegression()
model.fit(X_train,y_train)

predictions = model.predict(X_test)
#accuracy = confusion_matrix(y_test,predictions)
#print(accuracy)

accuracy = accuracy_score(y_test,predictions)
print(accuracy)

#print(predictions)


