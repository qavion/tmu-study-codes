#sh all_dev_bleu [model] [epoch] [reference]

sed -r 's/ //g' $3 | sed -r 's/_/ /g' > dev.reference

for i in $(seq -f %03g 1 $2)
    do
        echo "Model: $1.${i}"
        sed -r 's/ //g ' $1.${i}.dev_result | sed -r 's/_/ /g' > dev.result
        /clwork/yukio/YukioNMT/src/evaluation/multi-bleu.perl dev.reference < dev.result
    done

rm dev.reference
rm dev.result
