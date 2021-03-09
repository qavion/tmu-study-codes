#!/usr/bin/env python3

# remove_different_length.py [source] [source_bpe] [target_bpe] [scale_th(1<)]
# source <--> target

import sys

src_path = sys.argv[1]
src_bpe_path = sys.argv[2]
tgt_bpe_path = sys.argv[3]
scale_th = float(sys.argv[4])

src_bpe_buff = []
tgt_bpe_buff = []

# "~.cln1_2", "~.cln1_5"
suffix = '.cln' + str(scale_th).replace('.', '_')
src_f = open(src_bpe_path + suffix, 'w')
tgt_f = open(tgt_bpe_path + suffix, 'w')

for i, (src, src_bpe, tgt_bpe) in enumerate(zip(open(src_path), open(src_bpe_path), open(tgt_bpe_path))):
    if not i % 1000 and i:
        src_f.writelines(src_bpe_buff)
        tgt_f.writelines(tgt_bpe_buff)
        src_bpe_buff = []
        tgt_bpe_buff = []
    src_len = len(src.strip().split(' '))
    bpe_len = len(src_bpe.strip().split(' '))
    scale = bpe_len / float(src_len)
    # Skip if sentence length scale difference is big
    if scale >= scale_th:
        continue
    src_bpe_buff.append(src_bpe)
    tgt_bpe_buff.append(tgt_bpe)
else:
    # Write the rest and close
    src_f.writelines(src_bpe_buff)
    tgt_f.writelines(tgt_bpe_buff)
    src_f.close()
    tgt_f.close()
