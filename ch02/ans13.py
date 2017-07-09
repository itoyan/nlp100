#-*- coding:utf-8 -*-

'''
13. col1.txtとcol2.txtをマージ
    コマンドでは$ paste col1.txt col2.txt
'''

import io
import re

col1 = io.open('col1.txt', 'r', encoding='utf_8')
col2 = io.open('col2.txt', 'r', encoding='utf_8')
merge = io.open('merge.txt', 'w', encoding='utf_8')

pref = [re.sub(r'\n', '', w) for w in col1] #行末の改行コードを削除
city = [re.sub(r'\n', '', w) for w in col2]

for (p, c) in zip(pref, city):
    merge.write(p + "\t" + c + "\n")

# ファイルをすべて閉じる
col1.close()
col2.close()
merge.close()