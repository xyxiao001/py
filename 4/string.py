a = 'this'
print(len(a))
print(a[1])
print(a[-1])
# slice 1号位到3号位
print(a[1:3])
# 拷贝
print(a[:])
# 字符串单个字节不能修改

print(a.find('s'))

# replace 不能改变原始字符串
b = a.replace('i', 'a').replace('s', 't')
print(a, b)

#转大写
print(a.upper())

# 切割数组
print('a,b,c,d'.split(','))

# 正则
print('%a, eggs, and %a' %('this', 'THIS'))
