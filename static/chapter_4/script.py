import math
import random

title = "The Meaning of life"

print(math.pi)
print(math.sqrt(85))
print(random.random())
print(random.choice([1,2,3,4,5]))

print('--------------------------')
S = 'Spam'
len(S)
print('0 = ' + S[0])
print('1 = ' + S[1])
print('-1 = ' + S[-1])
print('-2 = ' + S[-2])
print('1:3 = ' + S[1:3])
print(': = ' + S[:])
print('1: = ' + S[1:])
print(':3 = ' + S[:3])
print(':-1 = ' + S[:-1])

print('--------------------------')
print(S.find('pa'))
print('s replace pa by XYZ = ' + S.replace('pa', 'XYZ') + ' and S = ' + S)

print('--------------------------')
line = 'aaa,bbb,ccccc,ddddd'
print(line.split(','))
S = 'spam'
print('s upper = ' + S.upper())
print(S.isalpha())
line = "dsf  s dfs   \n"
print("line = " + line)
line.rstrip()
line.lstrip()
print("line = " + line)

print('--------------------------')
print('%s upper is %s' % ('spam', 'SPAM!'))
print('{0} upper is {1}'.format('spam', 'SPAM!'))