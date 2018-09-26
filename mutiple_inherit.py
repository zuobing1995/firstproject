#mutiple_inherit.py
class Car:
    '''汽车'''
    def run(self,speed):
        print('汽车以%d公里/小时的速度行驶'%speed)
    def a(self):
        print('')
class Plane:
    '''飞机'''
    def fly(self,height):
        print('飞机以海拔%d米的高度飞行'%height)
    def a(self):
        
class Carplane(Car,Plane):
    '''carplane同时继承自car 和 Plane类'''
p=Carplane()
p.fly(10000)
p.run(300)