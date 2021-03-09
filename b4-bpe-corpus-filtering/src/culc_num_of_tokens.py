#!/usr/bin/env python3

# Compute the average of the number of tokens of one sentence

# culc_num_of_tokens.py [source(.ja)]

import sys

path = sys.argv[1]

buff = []
total_num = 0
line_count = 0

for line in open(path):
    num = len(line.strip().split())
    total_num += num
    line_count += 1

print('average:' + str(total_num / float(line_count)))
