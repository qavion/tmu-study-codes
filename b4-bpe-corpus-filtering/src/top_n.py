#!/usr/bin/env python3
# top_n.py [.json.out] [source_bpe] [target_bpe] [n]

import sys

arg_size = len(sys.argv)

if arg_size != 5:
    INPUT_FILENAME = '/clwork/homma/tmp/1million.json.out'
    SOURCE_FILENAME = 'train.bpe32k.cat.ja'
    TARGET_FILENAME = 'train.bpe32k.cat.en'
    SENTENCE_COUNT_TO_DELETE = 4030
else:
    INPUT_FILENAME = sys.argv[1]
    SOURCE_FILENAME = sys.argv[2]
    TARGET_FILENAME = sys.argv[3]
    SENTENCE_COUNT_TO_DELETE = int(sys.argv[4])

# Count the number of top n NEs.
with open(INPUT_FILENAME) as input_file:
    million_list = [int(i) for i in input_file if i != 0]
sorted_million = sorted(million_list, reverse=True)
top_n = sorted_million[:SENTENCE_COUNT_TO_DELETE]
threshold_value = top_n[-1]
thresholds_num = top_n.count(threshold_value)

# print(top_n)
print('threshold_value :', threshold_value)
print('thresholds_num :', thresholds_num)

# Read three files at the same time
# delete unnecessary sentences
# create Source and Target filtered by NER
input_file = open(INPUT_FILENAME)
source_file = open(SOURCE_FILENAME)
target_file = open(TARGET_FILENAME)
suffix = '.cln_ner'
source_out_file = open(SOURCE_FILENAME + suffix, 'w')
target_out_file = open(TARGET_FILENAME + suffix, 'w')

src_buff = []
tgt_buff = []

with input_file, source_file, target_file, source_out_file, target_out_file:
    for i, (num, src, tgt) in enumerate(zip(input_file, source_file, target_file)):
        if not i % 5000 and i:
            source_out_file.writelines(src_buff)
            target_out_file.writelines(tgt_buff)
            src_buff = []
            tgt_buff = []
        if int(num) > threshold_value:
            continue
        elif int(num) == threshold_value and thresholds_num:
            thresholds_num -= 1
            continue
        src_buff.append(src)
        tgt_buff.append(tgt)
    else:
        source_out_file.writelines(src_buff)
        target_out_file.writelines(tgt_buff)

