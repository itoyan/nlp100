#-*- coding:utf-8 -*-

'''
03. 円周率
'''

original = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
new_sentence = orig.replace(".", "").replace(",", "")

words_list = new_sentence.split(" ")
word_len = [ len(w) for w in wordslist ]

print word_len
