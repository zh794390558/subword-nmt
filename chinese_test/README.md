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

```
[zhanghui@TitanX92 chinese_test]$ head cut.txt ltp_cut.txt 
==> jieba_cut.txt <==
需要 知道 康提 茶业 的 地图 
湖上 初雨 是 谁 写 的 啊 
吃水果 后能 马上 喝茶 吗 
我 该 去 哪里 查询 转账 明细 
乘 什么 车到 岳和花苑 
明天 要 多 穿点 衣服 吗 
现在 的 油价 是 每升 八块 一毛 七 
今年 端午节 是 什么 时候 
政府 的 公务员 现在 太 舒服 了 钱 多事少 还 不用 担心 下岗 难怪 那么 多人 想 混进去 
哦 呵呵 那 你 现在 就 回来 吧 

==> ltp_cut.txt <==
需要 知道 康提 茶业 的 地图
湖 上 初雨 是 谁 写 的 啊
吃 水果 后 能 马上 喝茶 吗
我 该 去 哪里 查询 转账 明细
乘 什么 车 到 岳 和 花苑
明天 要 多 穿 点 衣服 吗
现在 的 油价 是 每 升 八 块 一 毛七
今年 端午节 是 什么 时候
政府 的 公务员 现在 太 舒服 了 钱 多事少 还 不用 担心 下岗 难怪 那么 多 人 想 混 进去
哦呵呵 那 你 现在 就 回来 吧

```
