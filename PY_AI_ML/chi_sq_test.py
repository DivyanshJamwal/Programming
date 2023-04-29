from cmath import exp
import scipy.stats as stats
from scipy.stats import chi2
import seaborn as sns
import pandas as pd
import numpy as np

data = sns.load_dataset('tips')
#print(data.head())

data_table = pd.crosstab(data['sex'],data['smoker'])
#print(data_table)

obs_val = data_table.values
#print('Observed Values : \n', obs_val)

val = stats.chi2_contingency(data_table)
#print(val)

exp_val = val[3]
n_rows = len(data_table.iloc[0:2,0])
n_cols = len(data_table.iloc[0,0:2])
ddof = (n_rows-1)*(n_cols-1)
#print("Degree of Freedom : ",ddof)
alpha = 0.05

chi_sq = sum([(o-e)**2./e for o,e in zip(obs_val,exp_val)])
chi_stats = chi_sq[0]+chi_sq[1]

#print("Chi Square Statistics : ", chi_stats)

crit_val = chi2.ppf(q=1-alpha,df=ddof)
#print('critical value : ', crit_val)

p_val = 1-chi2.cdf(x=chi_stats,df=ddof)

print("P-value : ",p_val)
print("Significance level : ",alpha)
print("Degree of freedom : ",ddof)
print("Critical value : ",crit_val)
 
if chi_stats >= crit_val:
    print("Reject H0. There is a relationship between 2 categorical variables")
else:
    print("Retain H0. There is no relationship between 2 categorical variables")

if p_val <= alpha:
    print("Reject H0. There is a relationship between 2 categorical variables")
else:
    print("Retain H0. There is no relationship between 2 categorical variables")