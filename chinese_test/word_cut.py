#!/usr/bin/env python
# coding:utf-8

from __future__ import unicode_literals 

import os
import sys
import codecs
import jieba

if __name__ == '__main__':

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
    
