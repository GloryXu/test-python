import re

match = re.match('Hello [\t]*(.*)world', 'Hello    Python world Hello Java world')
print(match.group(1))

match = re.match('/(.*)/(.*)/(.*)', '/usr/home/local')
print(match.groups())

print('-----------------------------------------')
L = [123,'spam', 1.23]
print(L[:-1])
print(L + [4,5,6])
print(L)
L.append('NI')
print(L)
print(L.pop(2)) # delete an item in the middle
print(L)

print('-----------------------------------------')
M = ['xx','aa','bb','ccc']
print(M.sort()) # None
print(M)
M.reverse()
print(M)

print('-----------------------------------------')
M = [[1,2,3],[4,5,6],[7,8,9]]
print(M)
print(M[1][2])