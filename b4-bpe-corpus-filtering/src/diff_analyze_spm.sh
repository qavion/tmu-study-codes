#!/bin/bash

# diff_analyze.sh [(bpe|spm)(N)k(|.cat)]

sh /work/homma/src/sentence_bleu.sh "/clwork/yamagishi/corpus/aspec/corpus.spm/test.${1}.en" "sample.test_result.beam1"

python /work/homma/src/bleu_scale.py test_sentence_bleu_result /work/homma/bpe/aspec_ja_en/baseline/nmt_ja_en/test_sentence_bleu_result

python /work/homma/src/top_worst_n.py "/clwork/yamagishi/corpus/aspec/corpus.cln/test.cln.ja" "/clwork/yamagishi/corpus/aspec/corpus.spm/test.${1}.ja"

python /work/homma/src/kendall.py "test.${1}.ja.lendiff" "sentbleu_scale"
