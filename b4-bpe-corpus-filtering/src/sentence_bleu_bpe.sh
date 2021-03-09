#sh sentence-bleu-bpe [reference] [system_out] 

sed -r 's/ //g' $2 | sed -r 's/▁/ /g'> test_out.tmp

/clwork/yukio/eval4eval/mosesdecoder/mert/sentence-bleu $1 < test_out.tmp > test_sentence_bleu_result

# /clwork/yukio/YukioNMT/src/evaluation/multi-bleu.perl dev.reference < dev.result

