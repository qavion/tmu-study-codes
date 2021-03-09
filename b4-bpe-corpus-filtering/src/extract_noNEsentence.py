#!/usr/bin/env python3
# extruct_noNEsentence.py

input_filename = '/clwork/homma/corpus/aspec/corpus.bpe/removed_cln1_5_en'
ner_filename = '/clwork/homma/tmp/remove_ner.json.out'

input_file = open(input_filename)
ner_file = open(ner_filename)
output_file = open(input_filename + '.noNE', 'w')

with ner_file, input_file, output_file:
    for sentence, ne in zip(input_file, ner_file):
        if not ne.startswith('0'):
            continue
        output_file.write(sentence)
