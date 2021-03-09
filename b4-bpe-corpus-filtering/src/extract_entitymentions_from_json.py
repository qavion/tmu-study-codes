#!/usr/bin/env python3

import ijson
import sys

if len(sys.argv) == 1:
    json_filename = 'input_15.txt.json'
else:
    json_filename = sys.argv[1]

with open(json_filename, 'rb') as input_file:
    parser = ijson.parse(input_file)
    entitymentions = ijson.items(input_file, 'sentences.item.entitymentions')
    for entitymention in entitymentions:
        print(len(entitymention))

