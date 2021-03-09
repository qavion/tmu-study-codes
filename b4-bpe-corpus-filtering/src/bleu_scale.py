#!/usr/bin/env python3

# bleu_scale.py [BPEsentencebleu] [sentencebleu]

import sys

path1 = sys.argv[1]
path2 = sys.argv[2]

buff = []

for l1, l2 in zip(open(path1), open(path2)):
    scale = float(l1.strip()) / float(l2.strip())
    buff.append(str(scale) + '\n')

with open('sentbleu_scale', 'w') as f:
    f.writelines(buff)
