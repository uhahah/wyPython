# -*- coding:utf-8 -*-
import numpy as np
from scipy.stats import chi2
mean = np.random.randn(2)
cov = np.eye(2)
nnull=(1,2,3)
result = np.random.multivariate_normal(mean, cov, nnull)
print(result)
nu=2
print("-------------------------")
result2 = np.random.multivariate_normal(mean, cov, nnull).T * np.sqrt(nu / chi2.rvs(nu,size=nnull))
print(result2)