# 复数
a = 2 + 1j
print(a*3) # 6+3j

#不同进制的数 16， 8 ， 2
b = 0x01
print(b)
# oct() 8  hex() 16  bin() 2
print(eval('int(8.5)'))
# Eval like JS to perform some of the string

# 8进制 0o1 16进制 0x1 2进制 0b1 相当于 10进制 1

# 位操作符都是转化为二进制进行操作
x = 1
x << 2 # 4
x | 2 # 3
x & 1 # 1


min(1,2,3,4) #1
max(1,2,3,4) #4
abs(-5)  # 5 绝对值
'{0: .2f}'.format(1/3) # 0.33
