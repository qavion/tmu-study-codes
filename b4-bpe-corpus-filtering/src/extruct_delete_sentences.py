#!/usr/bin/env python3

# extruct_delete_sentences.py before_deletion after_deletion

import sys

path1 = sys.argv[1]
path2 = sys.argv[2]

f_after = open(path2)

deleted_lines = []

for l_before in open(path1):
    while l_before != f_after.readline():
        deleted_lines.append(l_before)

with open('deleted_lines', 'w') as f:
    f.writelines(deleted_lines)
