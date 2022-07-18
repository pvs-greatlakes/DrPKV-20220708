# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import   scipy.stats as     stats
import   numpy       as     np
mu         =   90
sigma      =   1.6
n          =   64

ci95       =   stats.norm.interval(0.95, loc = mu, scale = sigma / np.sqrt(n))
print("\nZ score at 95% Confidence Level is  {0[0]:.2f}, {0[1]:.2f}".format(ci95))

ci99       =   stats.norm.interval(0.99, loc = mu, scale = sigma / np.sqrt(n))
print("\nZ score at 99% Confidence Level is  {0[0]:.2f}, {0[1]:.2f}".format(ci99))

import scipy.stats as stats
print("\nZ score at 99% Confidence Level is {0:0.2f}".format(stats.norm.ppf(.995)))

### END 1 ###

