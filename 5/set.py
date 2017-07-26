x= set('abcde')
y = set('bdxyz')
print(x)
print(y)
print('e' in x)
print(x - y)
print(x & y)
print(x ^ y)
print(x > y, x < y)
# intersection 是区两个集合相同的值
z = x.intersection(y)
print(z)
z.add('SPAM')
print(z)
z.update(set(['X', 'Y']))
print(z)
z.remove('b')
print(z)

for item in set('abc'): print(item * 3)

a = set('1234')
print(a)
b = set('23456')
# union 会过滤掉重复的值
c = a.union(b)
print(c)

d = {x ** 2 for x in [1, 2, 3, 4]}
print(d)

print(type(True))
