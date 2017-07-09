#-*- coding:utf-8 -*-

'''
14. 先頭からN行を出力
    python ans14.py 10 のように呼び出す。
    コマンドでは $ head -n 10 hightemp.txt
'''

import io
import sys

# 先頭の呼び出す行数が格納されている。引数のエラー処理はしていないので注意。
num = int(sys.argv[1])

hightemp = io.open('hightemp.txt', 'r',  encoding='utf_8_sig')

counter = 0
for line in hightemp:
    if( counter >= num ):
        break
    counter += 1
    print(line)


hightemp.close()
