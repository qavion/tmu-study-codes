# apply_bpe.py file
# BPEモデルを読み込んで入力ファイルに適用して、.bpeを間に追加して出力する
import sys

import sentencepiece as spm
from tqdm import tqdm

if len(sys.argv) != 2:
    raise 'コマンドライン引数にBPEを適用するファイルを一つだけ指定してね'

file_path = sys.argv[1]
bpe_path = file_path[:-4] + '.bpe' + file_path[-4:]

# Load model
sp = spm.SentencePieceProcessor()
sp.load('m_bpe.model')

# 変換して書き込み
with open(bpe_path, 'w') as f:
    for line in tqdm(open(file_path)):
        line = line.rstrip('\n')
        print(' '.join(sp.encode_as_pieces(line)), file=f)