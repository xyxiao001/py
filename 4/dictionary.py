#字典
d = {'a': 'food', 'b': 'phone', 'c': 'pen'}
print(d)

people = {
  'name': {'first': 'Bob', 'last': 'Smith'},
  'job': ['dev', 'mgr'],
  'age': 40.5
}
print(people)

people['job'].append('js')
print(people)

# 键的排序
ks = list(d.keys())
ks.sort()
for key in ks:
    print(key, '=>', d[key])

for key in sorted(d):
    print(key, '=>', d[key])

#while
x = 4
while x > 0:
    print('x!' * x)
    x -= 1

if not 'f' in d:
    print('missing')

print(d['x'] if 'x' in d else 0)
