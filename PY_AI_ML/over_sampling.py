import numpy as np
import pandas as pd
import imblearn
import sklearn
import scipy
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report,accuracy_score
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn.svm import OneClassSVM
from collections import Counter
from imblearn.under_sampling import NearMiss
from imblearn.over_sampling import RandomOverSampler
from imblearn.combine import SMOTETomek

RANDOM_SEED = 42
LABELS = ["Normal", "Fraud"]

data = pd.read_csv('C:\\Users\\Devil\\Documents\\Test_Data\\creditcard.csv')
#print(data.head())

columns = data.columns.tolist()
columns = [c for c in columns if c not in ['Class']]
target = "Class"
state = np.random.RandomState(42)
x = data[columns]
y = data[target]
x_outliers = state.uniform(low=0,high=1,size = (x.shape[0], x.shape[1]))

#print(x.shape)
#print(y.shape)

#print(data.isnull().values.any())
count_classes = pd.value_counts(data['Class'],sort = True)
count_classes.plot(kind = 'bar', rot = 0)

plt.title("Transaction Class Distribution")
plt.xticks(range(2), LABELS)
plt.xlabel("Class")
plt.ylabel("Frequency")
#plt.show()

fraud = data[data['Class']==1]
normal = data[data['Class']==0]

#print(fraud.shape,normal.shape)

smk = SMOTETomek()
x_res,y_res = smk.fit_resample(x,y)

#print(x_res.shape,y_res.shape)

#print('Original dataset shape {}'.format(Counter(y)))
#print('Resampled dataset shape {}'.format(Counter(y_res)))

os = RandomOverSampler(ratio=1)
X_train_res,y_train_res = os.fit_sample(x,y)

#print('Original dataset shape {}'.format(Counter(y)))
#print('Resampled dataset shape {}'.format(Counter(y_train_res)))
