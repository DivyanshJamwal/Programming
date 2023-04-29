import matplotlib.pyplot as plt
import seaborn as sns
df=sns.load_dataset("tips")

#print(df.head()) #-- dataset
#print(df.dtypes) #-- datatypes of features

#print(df.corr())  #-- correlation b/w features
#print(sns.heatmap(df.corr()))  #-- heatmap

#print(sns.jointplot(x='tip',y='total_bill',data=df,kind='hex')) #-- jointplot
#print(sns.pairplot(df)) #-- pairplot
#print(sns.pairplot(df,hue='smoker')) #-- pairplot(specific)
#print(df['smoker'].value_counts()) #-- count of feature
#print(sns.displot(df['tip'])) #-- displot
#print(sns.countplot('day',data=df)) #-- countplot
#print(sns.barplot(x='sex',y='total_bill',data=df)) #-- barplot
#print(sns.boxplot('sex','total_bill',data=df)) #-- boxplot
#print(sns.violinplot('sex','total_bill',hue='smoker',data=df,palette='rainbow')) #-- violinplot
plt.show()