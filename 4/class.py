# 用户定义的类
class Worker:
    def  __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

bob = Worker('Bob Smith', 50000)
sue = Worker('Sue Joned', 60000)
print(bob.lastName())
sue.giveRaise(0.11)
print(sue.pay)
# 隐式的self 指向自己
