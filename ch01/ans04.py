#-*- coding:utf-8 -*-

'''
04. 元素記号
'''

original = "Hi He Lied Because Boron Could Not Oxidize Fluorine. " \
    "New Nations Might Also Sign Peace Security Clause. Arthur King Can."
wordList = original.replace(".", "").split(" ")

# wordListから何番目の配列の要素だけを1文字目だけ取り出すか指定
single = [1, 5, 6, 7, 8, 9, 15, 16, 19]

chemicalSymbol = {}

for word, idx in zip(wordList, range(1, len(wordList))):
    length = 1 if idx in single else 2 # 3項演算子
    chemicalSymbol.update({word[0:length]:idx})

print chemicalSymbol
