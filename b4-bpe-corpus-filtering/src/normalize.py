# python normalize.py file1 [file2 ...]
import sys

import mojimoji
from tqdm import tqdm

file_paths = sys.argv[1:]

fitr = file_paths if len(file_paths) <= 1 else tqdm(file_paths)

for f_input in fitr:
    file_name, file_ext = f_input.rsplit('.', 1)
    f_output = '.'.join([file_name, 'mjmj', file_ext])

    with open(f_output, 'w') as f:
        for line in open(f_input):
            line = line.rstrip()
            print(mojimoji.zen_to_han(line), file=f)