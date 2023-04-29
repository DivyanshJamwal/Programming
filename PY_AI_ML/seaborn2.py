import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset('iris')
#print(iris.head())
#print(iris.dtypes)

#sns.pairplot(iris)
#sns.jointplot(x='sepal_length',y='sepal_width',data=iris)
#sns.displot(iris['petal_length'])
#(sns.countplot('petal_length',data=iris)
#sns.barplot(x='petal_length',y='sepal_length',data=iris)
#sns.boxplot('petal_length','sepal_width',hue='species',data=iris,palette='rainbow')
#sns.violinplot(x='sepal_length',y='sepal_width',hue='species',data=iris,palette='rainbow')
plt.show()