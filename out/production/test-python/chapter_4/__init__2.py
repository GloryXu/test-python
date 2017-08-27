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

