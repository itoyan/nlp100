#-*- coding:utf-8 -*-

'''
07. テンプレートによる文生成
'''

def informYisZatX(x, y, z):
    return u'%s時の%sは%s' % (x, y, z)

x=12
y=u"気温"
z=22.4

print informTime(x, y, z)
