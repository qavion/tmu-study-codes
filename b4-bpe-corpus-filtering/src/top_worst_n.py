#!/usr/bin/env python3

# top_worst_n.py test.spmNk.ja test.cln.ja [n]

import os
import sys

path1 = sys.argv[1]
path2 = sys.argv[2]
if len(sys.argv) > 3:
    n = int(sys.argv[3])
else:
    n = 50

buff = []
diffs = []
for i, (l1, l2) in enumerate(zip(open(path1), open(path2))):
    diff = len(l1.strip().split(' ')) / float(len(l2.strip().split(' ')))

    buff.append(str(diff) + '\n')
    diffs.append((diff, i))

with open(os.path.basename(path1) + '.lendiff', 'w') as f:
    f.writelines(buff)

diffs.sort()
with open('idx_lendiff_top{}'.format(n), 'w') as f:
    f.writelines(('{}\t{}\n'.format(i, d) for d, i in diffs[:n]))
with open('idx_lendiff_worst{}'.format(n), 'w') as f:
    f.writelines(('{}\t{}\n'.format(i, d) for d, i in diffs[-n:]))

