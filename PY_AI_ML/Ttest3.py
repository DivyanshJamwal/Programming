import pandas as pd
import numpy as np
import scipy.stats as stats
import math

np.random.seed(6)
classA_ages = stats.poisson.rvs(loc=18,mu=30,size=60)

np.random.seed(12)
classB_ages = stats.poisson.rvs(loc=18,mu=33,size=60)
#print(classB_ages.mean())

_,p_value = stats.ttest_ind(a=classA_ages,b=classB_ages,equal_var=False)
#print(school_ages.mean())

if p_value < 0.05:
    print("We are rejecting Null Hypothesis")
else:
    print("We are accepting Null Hypothesis")
