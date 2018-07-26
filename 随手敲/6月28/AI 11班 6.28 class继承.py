class Animal:
    def eat(self):
        print('吃饭')
    def drink(self):
        print('喝水')
class Mammalia(Animal):
    def milk(self):
        print('哺乳')
class Birds(Animal):
    def fly(self):
        print('飞翔')
class Dog(Mammalia):
    def __init__(self,name,daxiao):
        self.name=name
        self.daxiao=daxiao
    def run(self):
        print('奔跑')
class Bianfu(Birds,Mammalia):
    def __init__(self,name,daxiao):
        self.name=name
        self.daxiao=daxiao
    def sn(self):
        print('接收超声波')
    
a=Dog('小黄','小')
b=Bianfu('大黑','大')
c=Dog('旺财','大')
d=Bianfu('小灰','小')
