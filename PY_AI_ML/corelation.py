import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset('iris')
print(df.corr())

print(sns.pairplot(df))
plt.show()