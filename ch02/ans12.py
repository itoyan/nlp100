#-*- coding:utf-8 -*-

'''
12. 1列目をcol1.txtに，2列目をcol2.txtに保存
    コマンドでは
    $ cat hightemp.txt | cut -f 1 > col1.txt
    $ cat hightemp.txt | cut -f 2 > col2.txt
'''

import io
import re

fin = io.open('hightemp.txt', 'r',  encoding='utf_8_sig')
col1 = io.open('col1.txt', 'w', encoding='utf_8')
col2 = io.open('col2.txt', 'w', encoding='utf_8')


for line in fin:
    placelist = line.split("\t")
    col1.write(placelist[0] + "\n")
    col2.write(placelist[1] + "\n")


# ファイルをすべて閉じる
fin.close()
col1.close()
col2.close()
