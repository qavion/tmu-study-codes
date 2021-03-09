#!/bin/bash

# diff_analyze.sh [(spm|bpe)(N)k(|.cat)]

sh /work/homma/src/sentence_bleu_bpe.sh "/clwork/yamagishi/corpus/aspec/corpus.spm/test.${1}.en" "sample.test_result.beam1"

python /work/homma/src/top_worst_n.py "/clwork/yamagishi/corpus/aspec/corpus.cln/test.cln.ja" "/clwork/yamagishi/corpus/aspec/corpus.spm/test.${1}.ja"

python /work/homma/src/kendall.py "test.${1}.ja.lendiff" "test_sentence_bleu_result"