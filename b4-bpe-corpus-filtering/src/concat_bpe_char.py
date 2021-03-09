# concat_bpe.py train.tok.src train.tok.trg
# 2ファイルを結合してBPEモデルと文字レベルを同時に学習
# sentencepieceによる文字正規化も行う

import sys

import sentencepiece as spm

if len(sys.argv) != 3:
    raise '引数のファイル数がおかしいよ！srcとtrgファイルを入れてね'

src_path = sys.argv[1]
trg_path = sys.argv[2]

concat_path = src_path + '.trg.concat'
with open(concat_path, 'w') as out:
    for l in open(src_path):
        print(l.rstrip('\n'), file=out)
    for l in open(trg_path):
        print(l.rstrip('\n'), file=out)

# model training and saving
params = [
    '--input=' + concat_path,
    '--model_type=bpe', # bpe
    '--model_prefix=m_bpe',
    '--vocab_size=30000', # vocabraly size → 30,000
    '--hard_vocab_limit=false', # エラー回避
    '--normalization_rule_name=nfkc_cf', # nfkc + Unicode case folding
]
spm.SentencePieceTrainer.Train(' '.join(params))

params = [
    '--input=' + concat_path,
    '--model_type=char', # char
    '--model_prefix=m_char',
    '--vocab_size=30000', # vocabraly size → 30,000
    '--hard_vocab_limit=false', # エラー回避
    '--normalization_rule_name=nfkc_cf', # nfkc + Unicode case folding
]
spm.SentencePieceTrainer.Train(' '.join(params))