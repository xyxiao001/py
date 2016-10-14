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

num = [1, 3, 4, 5, 8, 9]
num.sort()
print(num)
num.reverse()
print(num)

#数组嵌套
m = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
print(m)

col1 = [row[0] for row in m]
col2 = [row[1] for row in m]
print(col1)
print(col2)
# 取值第三竖行的能整除2的
print([row[2] for row in m if row[2] % 2 == 0])

# 取得矩阵 1 5 9
dig = [m[i][i] for i in [0, 1, 2]]
print(dig)


# 算出每项的和
g = (sum(row) for row in m)
print(next(g))
print(next(g))

print(list(map(sum, m)))

print({sum(row) for row in m})

print({x: ord(x) for x in 'span'})
