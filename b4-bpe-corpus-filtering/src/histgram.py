#!/usr/bin/env python3
# histgram.py [input_file_path]

import sys
from collections import defaultdict

file_path = sys.argv[1]

hist_dict = defaultdict(int)
hist_dict_bi = defaultdict(int)
f = open(file_path)
with f:
    for line in f:
        subwords = line.strip().split('')
        for subword in subwords:
            hist_dict[subword] += 1
            l = len(subword)
            if l <= 2 or (subword.startswith('▁') and l) == 3:
                hist_dict_bi[subword] += 1

out_all_f = open(file_path + '.allwordhist', 'w')
out_bi_f = open(file_path + '.bi-wordhist', 'w')
with out_all_f, out_bi_f:
    for k, v in sorted(hist_dict.items(), key=lambda x: -x[1]):
        out_all_f.write(f'{k}\t{v}\n')
    for k, v in sorted(hist_dict_bi.items(), key=lambda x: -x[1]):
        out_bi_f.write(f'{k}\t{v}\n')

