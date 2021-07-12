import scipy.stats.norm.cdf

mu = 178
sigma = 7.7
dist = scipy.stats.norm.cdf(loc=mu, scale=sigma)
type(dist)

dist.mean(178), dist.std(7.7)

dist.cdf(mu-sigma)

low = dist.cdf(177.8)    # 5'10"
high = dist.cdf(185.4)   # 6'1"
low, high, high-low

##pareto distribution
alpha = 1.7
xmin = 1       # meter
dist = scipy.stats.pareto(b=alpha, scale=xmin)
dist.median()

dist.mean()

dist.cdf(dist.mean())

(1 - dist.cdf(1000)) * 7e9, dist.sf(1000) * 7e9

dist.sf(600000) * 7e9

dist.ppf(1 - 1/7e9)