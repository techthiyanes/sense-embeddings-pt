# Student's t-test for independent samples
from numpy.random import seed
from numpy.random import randn
from scipy.stats import ttest_ind
from scipy.stats import t
from xml.dom import minidom

def read_xml(filename):
    """Docstring."""
    data = []
    with open(filename) as fp:
        xml = minidom.parse(fp)
    pairs = xml.getElementsByTagName('pair')
    for pair in pairs:
        data.append(float(pair.getAttribute('similarity')))
    return data

# generate two independent samples
# seed the random number generator
#seed(1)
# generate two independent samples
data1 = [14.4, 22, 66.7, 17.7, 82.8, 69.2, 53.3, 44.0, 47.8]
data2 = [11, 23.1, 60, 14.1, 80.6, 73.7, 62.9, 49.4, 51.6]

print('data1: ', len(data1))
print('data2: ', len(data2))

# compare samples
stat, p = ttest_ind(data1, data2, equal_var = False)
print('t=%.3f, p=%.3f' % (stat, p))

# degrees of freedom
df = len(data1) + len(data2) - 2

# calculate the critical value
alpha = 0.05
cv = t.ppf(1.0 - alpha, df)
print('cv: ', cv)

# calculate the p-value
p = (1.0 - t.cdf(abs(stat), df)) * 2.0
print('p: ', p)

# interpret via critical value
if abs(stat) <= cv:
    print('Accept null hypothesis that the means are equal.')
else:
    print('Reject the null hypothesis that the means are equal.')

# interpret via p-value
if p > alpha:
    print('Accept null hypothesis that the means are equal.')
else:
    print('Reject the null hypothesis that the means are equal.')