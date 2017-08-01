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

cols = [row[1] for row in M]
print(cols)

cols1 = [row[1] +1 for row in M]
print(cols1)

cols2 = [row[1] for row in M if row[1] % 2 != 0]
print(cols2)

diag = [M[i][i] for i in [0,1,2]]
print(diag)

doubles = [c * 2 for c in 'spam']
print(doubles)

G = (sum(row) for row in M)
print(next(G))
print(next(G))

print("----------------------")
print(list(map(sum,M)))

print("create a set of row sums")
# create a set of row sums
tem = {sum(row) for row in M}
print(tem)

print("create key/value table of row sums")
# create key/value table of row sums
tem2 = {i : sum(M[i]) for i in range(3)}
print(tem2)

print("List of character ordinals")
tem3 = [ord(x) for x in "spaam"]
print(tem3)

print("Set remove duplicates")
tem4 = {ord(x) for x in "spaam"}
print(tem4)

print("Dictionary keys are unique")
tem5 = {x : ord(x) for x in "spmmmd"}
print(tem5)

D = {'food':'Spam', 'quantity':4, 'color':'pink'}
print('Fatch value of key \'food\'')
print(D['food'])

print('Add 1 to \'quantity\' value')
D['quantity'] += 1
print(D)

F = {}
print('create keys by assignment')
F['name']='xugr'
F['sex']='fale'
print(F)

