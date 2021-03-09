#!/usr/bin/env python3

import sys
import random

tgt_infile_path = '/clwork/homma/corpus/aspec/corpus.bpe/train.bpe32k.cat.en'
src_infile_path = '/clwork/homma/corpus/aspec/corpus.bpe/train.bpe32k.cat.ja'
suffix = '.cln_rand'
sentence_num = 977367
deleted_sentences = 4030

tgt_outfile_path = tgt_infile_path + suffix
src_outfile_path = src_infile_path + suffix

tgt_infile = open(tgt_infile_path)
src_infile = open(src_infile_path)
tgt_outfile = open(tgt_outfile_path, 'w')
src_outfile = open(src_outfile_path, 'w')

ignore_nums = random.sample(range(sentence_num), deleted_sentences)

with tgt_infile, src_infile, tgt_outfile, src_outfile:
    for i, (tgt, src) in enumerate(zip(tgt_infile, src_infile)):
        if i in ignore_nums:
            continue
        tgt_outfile.write(tgt)
        src_outfile.write(src)

