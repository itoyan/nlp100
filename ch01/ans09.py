#-*- coding:utf-8 -*-

'''
09. Typoglycemia
'''

import random

class SentenceManipulation():
    '''
        文字列操作のためのクラス
    '''

    def __init__(self):
        self.sentence = ""

    def getSentence(self):
        return self.sentence

    def setSentence(self, sentence):
        self.sentence = sentence

    def typoglycemia(self):
        wordList = self.sentence.split()
        generatedSentence = ""
        for w in wordList:
            if len(w) <= 4:
                generatedSentence += w
            else:
                idx = range(1, len(w)-1)
                random.shuffle(idx)
                randomizedIdx = [0] +  idx + [len(w)-1]
                generatedWord = ""
                for i in randomizedIdx:
                    generatedWord += w[i]
                # print generatedWord
                generatedSentence += generatedWord
            generatedSentence += " "
        return generatedSentence[:len(generatedSentence)-1]


testString = "I couldn't believe that I could actually understand " +\
    "what I was reading : the phenomenal power of the human mind ."
sm = SentenceManipulation()
sm.setSentence(testString)
print sm.typoglycemia()
