# cmds

`pip install -r requirements.txt --user` to install segment word tools: jieba or pyltp

`word_cut.py`: from `chineses.txt` to `cut.txt`

`get_vocab.py`: from `cut.txt` to `vocab.txt` 

`learn_bpe.py`: from `vocab.txt` to `bpe.model`

`apply_bpe.py`: from `chineses.txt` to `cut_bpe.txt`


```
# pip install -r requirements.txt  --user
# ./word_cut.py chinese.txt 
# ../get_vocab.py < cut.txt > vocab.txt
# cat vocab.txt 
# ../learn_bpe.py -h
# ../learn_bpe.py -i vocab.txt -o bpe.model -s 40 -v --min-frequency 1
# vi bpe.model 
# vi vocab.txt  
# ../apply_bpe.py -h
# ../apply_bpe.py -i cut.txt -c bpe.model 
# ../apply_bpe.py -i cut.txt -c bpe.model -s '_'
# cat cut.txt 
# ../apply_bpe.py -i cut.txt -c bpe.model -s '_' -o cut_bpe.txt
# cat cut_bpe.txt 
# ../apply_bpe.py -i cut.txt -c bpe.model -s '_' -o cut_bpe.txt --vocabulary vocab.txt 

```
