#sh test_bleu_bpe.sh [test_result] [reference]

sed -r 's/ //g' $2 | sed -r 's/▁/ /g' > test.reference
sed -r 's/ //g ' $1 | sed -r 's/▁/ /g' > test.result

/clwork/yukio/YukioNMT/src/evaluation/multi-bleu.perl test.reference < test.result

rm test.reference
rm test.result
