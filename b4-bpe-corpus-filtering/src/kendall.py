#!/usr/bin/env python3

# kendall2.py *.lendiff test_sentence_bleu_result

from scipy import stats

import sys

path1 = sys.argv[1]
path2 = sys.argv[2]

buff1 = []
buff2 = []
for l1, l2 in zip(open(path1), open(path2)):
    buff1.append(float(l1.strip()))
    buff2.append(float(l2.strip()))

tau, p_value = stats.kendalltau(buff1, buff2)

print('kendall = ' + str(tau))

with open(path1 + '_sentBLEU.kendall', 'w') as f:
    f.write('tau = ' + str(tau) + '\n')
    f.write('p_value = ' + str(p_value) + '\n')
