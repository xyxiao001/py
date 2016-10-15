# 文件操作
# 创建文件 并指定可以写入
# f = open('data.txt', 'w')
# f.write('python create\n')
# f.close()

# 读取文件内容
f = open('data.txt')
# read 读取所有。 readline 读取一行
text = f.read()
print(text)
print(text.split())

data = open('data.bin', 'rb').read()
print(data)
print(data[4:8])

#集合
x = set('spam')
y = {'h', 'a', 'm'}
print(x, y)

print(x & y)
print(x | y)
print({x ** 2 for x in [1, 2, 3, 4]})

# 高精确度
import decimal
d = 1.1012
print(d + 1.202)
print(type(d))


#检验方法 isinstance(d, float) 会破坏代码灵活性
