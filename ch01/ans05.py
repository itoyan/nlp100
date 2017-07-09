#-*- coding:utf-8 -*-

'''
05. n-gram
'''

def n_gram(seq, n, typeStr):
    if typeStr == "list": # 文字列を単語単位のリストとして扱う
        seq = seq.split()
    elif typeStr == "str": # 1つの文字列として扱う
        seq = list(seq.replace(" ",""))
    else:
        return None
    return [ seq[i:(i+n)] for i in range(0, len(seq)-n+1) ]



testStr = "I am an NLPer"
#
print n_gram(testStr, 2, "list")
print n_gram(testStr, 2, "str")
