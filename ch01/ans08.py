#-*- coding:utf-8 -*-

'''
08. 暗号文
'''

def cipher(s):
    ciphered = ''
    for c in s:
        if str.islower(c):
            ciphered += chr(219 - ord(c))
        else:
            ciphered += c
    return ciphered

testString = '219-CharacterCode'
cString = cipher(testString) # 暗号化された文字列
c2String = cipher(cString) # もう1回暗号化
print cString
print c2String # testStringに戻っている

