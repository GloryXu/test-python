D = {'a':1, 'b':2, 'c':3}
Ks = list(D.keys())
print('Unordered keys list')
print(Ks)

Ks.sort()
print('keys sorted!')
print(Ks)

for key in Ks:
    print(key, '=>', D[key])

print(D)
for key in sorted(D):
    print(key, '=>', D[key])

x = 4
while x>0:
    print('spam!' * x)
    x -= 1

squares = [x ** 2 for x in [1,2,3,4,5]]
print(squares)
print('it is equal as below! for loop')
squares = []
for x in [1,2,3,4,5]:
    squares.append(x ** 2)
print(squares)

print('f' in D)

if not 'f' in D:
    print('missing')

print('Index but with a default')
print(D.get('x', 0))

print('if/else expression form')
value = D['x'] if 'x' in D else 1
print(value)

print('A 4-item tuple')
T = (1,2,3,4)
print(len(T))

print('Concatenation')
T = T + (5,6)
print(T)

print('Indexing ,slicing, and more')
print(T[0])

print('Tuple methods : 4 appears at offset 3')
print(T.index(4))

print('4 appears once')
print(T.count(4))

# Tuples are immutable.一旦创建就不可改变，不可变序列

# Throw Exception
#T[0] = 2
#print(T)