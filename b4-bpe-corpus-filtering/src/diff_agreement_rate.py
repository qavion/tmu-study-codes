#!/usr/bin/env python3
# diff_agreement_rate.py [input_file_path1] [input_file_path2] [n]

import sys

file_path1 = sys.argv[1]
file_path2 = sys.argv[2]
n = int(sys.argv[3])

with open(file_path1) as file1, open(file_path2) as file2:
    count = 0
    line_count = 0
    for line1, line2 in zip(file1, file2):
        num1 = int(line1)
        num2 = int(line2)
        if abs(num1 - num2) <= n:
            count += 1
        line_count += 1
    print(f'文長の差が{n}以下の行数: {count}, 一致率={count / line_count}')
