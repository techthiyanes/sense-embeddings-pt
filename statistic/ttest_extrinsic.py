# Student's t-test for independent samples
from numpy.random import seed
from numpy.random import randn
from scipy.stats import ttest_ind
from scipy.stats import t
from xml.dom import minidom
import statistics
from scipy.stats import mstats

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
#data1 = 5 * randn(100) + 50
#data2 = 5 * randn(100) + 51

#data2 = read_xml('/home/jessica/Documentos/UFSCar/Pesquisa/Projeto/portuguese_word_embeddings/sentence_similarity/data/assin-test-gold/assin-ptbr-test.xml')
data1 = read_xml('/home/jessica/Documentos/UFSCar/Pesquisa/Projeto/gitoficial/sense-embeddings-pt/datasets/sentence_similarity/data/output-elmo.xml')
data2 = read_xml('/home/jessica/Documentos/UFSCar/Pesquisa/Projeto/gitoficial/sense-embeddings-pt/datasets/sentence_similarity/data/output-mssg.xml')
data3 = read_xml('/home/jessica/Documentos/UFSCar/Pesquisa/Projeto/gitoficial/sense-embeddings-pt/datasets/sentence_similarity/data/output-glove.xml')

print("Data1: ", len(data1))
print("Data2: ", len(data2))

print("Data1: ", sum(data1))
print("Data2: ", sum(data2))

print("Mean of data1 is: ", statistics.mean(data1))
print("Mean of data2 is: ", statistics.mean(data2))

print("Variance of data1 is: ", statistics.variance(data1))
print("Variance of data2 is: ", statistics.variance(data2))

# kruskalwallis
H, pval = mstats.kruskalwallis(data1, data2, data3)

print("H-statistic:", H)
print("P-Value:", pval)

if pval < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")

# compare samples
stat, p = ttest_ind(data1, data2, equal_var=False)
print('t-statistic=%.3f, p-value=%.3f' % (stat, p))

# degrees of freedom
df = len(data1) + len(data2) - 2

# calculate the critical value
alpha = 0.05
print('alpha: ', alpha)
cv = t.ppf(1.0 - alpha, df)
print('critical-value: ', cv)

# calculate the p-value
p = (1.0 - t.cdf(abs(stat), df)) * 2.0
#print('p: ', p)

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