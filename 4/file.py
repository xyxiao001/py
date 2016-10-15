# 文件操作
# 创建文件 并指定可以写入
f = open('data.txt', 'w')
f.write('python create\n')
f.close()

# 读取文件内容
f = open('data.txt')
text = f.read()
print(text)
print(text.split())
