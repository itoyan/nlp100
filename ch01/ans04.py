#-*- coding:utf-8 -*-

'''
04. 元素記号
'''

original = "Hi He Lied Because Boron Could Not Oxidize Fluorine. " \
    "New Nations Might Also Sign Peace Security Clause. Arthur King Can."
wordList = original.replace(".", "").split(" ")

# 配列の中から1文字目だけ取り出す添字(1から始まる)を指定
single = [1, 5, 6, 7, 8, 9, 15, 16, 19]

chemicalSymbol = {}

# for word, idx in zip(wordList, range(1, len(wordList))):
for idx, word in enumerate(wordList):
    length = 1 if idx+1 in single else 2 # 3項演算子
    chemicalSymbol.update({word[0:length]:idx+1})

print chemicalSymbol
