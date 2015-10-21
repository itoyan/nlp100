#-*- coding:utf-8 -*-

'''
10. 行数のカウント
    コマンドで確認するときは次のようにする
    $ wc -l hightemp.txt
'''

import io

f = io.open('hightemp.txt', 'r',  encoding='utf_8_sig')
nLine = 0
for line in f:
    nLine += 1

f.close()
print nLine
