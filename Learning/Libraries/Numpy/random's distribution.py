from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')
sns.distplot(random.poisson(lam=10, size=1000), hist=False, label='poisson')
sns.distplot(random.uniform(size=1000), hist=False,label='uniform')
sns.distplot(random.logistic(size=1000), hist=False, label='logistic')
sns.distplot(random.exponential(size=1000), hist=False,label='exponential')
sns.distplot(random.chisquare(df=1, size=1000), hist=False,label='chisquare')
sns.distplot(random.rayleigh(size=1000), hist=False,label='rayleigh')
sns.distplot(random.pareto(a=2, size=1000), kde=False,label='pareto')
x = random.zipf(a=2, size=1000)
sns.distplot(x[x<10], kde=False,label='zipf')
plt.show()