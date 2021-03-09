#!/usr/bin/env python3
# statistic_float.py [file_path]

import sys

file_path = sys.argv[1]
with open(file_path) as f:
    sum_ = 0
    line_ = 0
    max_ = 0
    for l in f:
        n = float(l.strip())
        sum_ += n
        line_ += 1
        if max_ < n:
            max_ = n
    average = sum_ / line_
    print('avarage =', average)
    print('sum = ', sum_)
    print('line = ', line_)
    print('max = ', max_)
