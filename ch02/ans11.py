#-*- coding:utf-8 -*-

'''
11. タブをスペースに置換
    コマンドで確認するときは次のようにする
'''

import io
import re

fin = io.open('hightemp.txt', 'r',  encoding='utf_8_sig')
# 解答の出力先
fout = io.open('ans11.txt', 'w',  encoding='utf_8_sig')
for line in fin:
    re.sub(r' ', '\t', line) # 空白をタブに置換
    fout.write(line)

fin.close()
fout.close()
