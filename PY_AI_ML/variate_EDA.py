import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

iris = sns.load_dataset('iris')
#print(iris.head())

iris_setosa = iris.loc[iris['species']=='setosa']
iris_virginica = iris.loc[iris['species']=='virginica']
iris_versicolor = iris.loc[iris['species']=='versicolor']

#print(iris_setosa)
#print(iris_virginica) #-- print df with species
#print(iris_versicolor)

## UNIVARIATE ANALYSIS

plt.plot(iris_setosa['sepal_length'],np.zeros_like(iris_setosa['sepal_length']),'o')
plt.plot(iris_virginica['sepal_length'],np.zeros_like(iris_virginica['sepal_length']),'o')
plt.plot(iris_versicolor['sepal_length'],np.zeros_like(iris_versicolor['sepal_length']),'o')
plt.xlabel('Sepal Length')

## BIVARIATE ANALYSIS

sns.FacetGrid(iris,hue='species',height=5).map(plt.scatter,'sepal_length','sepal_width').add_legend()

## MULTIVARIATE ANALYSIS

sns.pairplot(iris,hue='species')
plt.show()



