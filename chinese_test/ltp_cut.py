#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from __future__ import unicode_literals 

import sys, os
import codecs 


# Set your own model path
ROOTDIR='/lustre/atlas/zhanghui/data/ltp_data'
MODELDIR=os.path.join(ROOTDIR, "ltp_data_v3.4.0")

from pyltp import SentenceSplitter, Segmentor, Postagger, Parser, NamedEntityRecognizer, SementicRoleLabeller

paragraph = '中国进出口银行与中国银行加强合作。中国进出口银行与中国银行加强合作！'

print(type(paragraph))

sentence = SentenceSplitter.split(paragraph)[0]

segmentor = Segmentor()
segmentor.load(os.path.join(MODELDIR, "cws.model"))
words = segmentor.segment(sentence)
print("\t".join(words))


if __name__ == '__main__':

   filename = sys.argv[1]
   #fout = codecs.open('cut.txt', mode='w', encoding='utf-8')
   fout = open('ltp_cut.txt', mode='w')
   with open(filename, 'r') as f:
       for l in f:
            cuts = list(segmentor.segment(l))
            print(cuts)
            fout.write(' '.join(cuts) + '\n')

   fout.close()
   sys.exit(0) 

   # python 2/3 compatibility
   if sys.version_info < (3, 0):
        sys.stderr = codecs.getwriter('UTF-8')(sys.stderr)
        sys.stdout = codecs.getwriter('UTF-8')(sys.stdout)
        sys.stdin = codecs.getreader('UTF-8')(sys.stdin)
   else:
        sys.stderr = codecs.getwriter('UTF-8')(sys.stderr.buffer)
        sys.stdout = codecs.getwriter('UTF-8')(sys.stdout.buffer)
        sys.stdin = codecs.getreader('UTF-8')(sys.stdin.buffer)

   filename = sys.argv[1]
   fobj = codecs.open(filename, 'r', encoding='utf-8')
   fout = codecs.open('cut.txt', mode='w', encoding='utf-8')

   for l in fobj:
       # jieba 
       cuts = list(jieba.cut(l))
       print(cuts)
       fout.write(' '.join(cuts))

   fobj.close()
   fout.close()
    
