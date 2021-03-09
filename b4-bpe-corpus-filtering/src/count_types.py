# count_types.py [target file]

import sys
import os.path


def count_type_token(fn):
    types = set()
    token_num = 0
    # file check
    if not os.path.isfile(fn):
        return None, None
    # count type and token
    for line in open(fn):
        words = line.strip().split()
        types.update(words)
        token_num += len(words)
    return len(types), token_num

tgtfilename = sys.argv[1]

type_num, token_num = count_type_token(tgtfilename)
print('type num:', type_num)
print('token num:', token_num)
