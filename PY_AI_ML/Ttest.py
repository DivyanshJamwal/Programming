from random import sample
import numpy as np
from scipy.stats import ttest_1samp

ages = [10,20,35,50,28,40,55,18,16,55,30,25,43,18,13,28,43,12,30,65,43,23,19,20,14,16,17,27,70]
#print(len(ages))

ages_mean = np.mean(ages)
#print(ages_mean)

sample_size = 10
age_sample = np.random.choice(ages,sample_size)
#print(age_sample)

ttest,p_value= ttest_1samp(age_sample,30)
#print(p_value)

if p_value < 0.05:
    print("We are rejecting Null Hypothesis")
else:
    print("We are accepting Null Hypothesis")

