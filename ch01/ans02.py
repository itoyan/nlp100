#-*- coding:utf-8 -*-

'''
02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
'''

patrolcar = u'パトカー'
taxi = u'タクシー'
merge = ''

for i in range(0, len(patrolcar)):
    merge += patrolcar[i]
    merge += taxi[i]

print merge
