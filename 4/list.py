# 列表 索引从0开始
L = [123, 'spam', 123]
print(L)
print(len(L))

print(L[0])
print(L[:-1])

print(L + [4, 5, 6])

# 数组尾部添加
L.append('7')
print(L)

# 删除索引第二位
L.pop(2)
print(L)
