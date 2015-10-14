#-*- coding:utf-8 -*-

'''
06. 集合
'''

# デフォルトは単語に対してbi-gramを返す
def findNgramSet(string, n=2):
    return [ string[i:(i+n)] for i in range(0, len(string)-n+1) ]

phraseA = "paraparaparadise"
phraseB = "paragraph"

X = set(findNgramSet(phraseA))
Y = set(findNgramSet(phraseB))

union = X.union(Y) # 和集合
intersection = X.intersection(Y) # 積集合
diff = X.difference(Y) # 差集合

print union
print intersection
print diff
