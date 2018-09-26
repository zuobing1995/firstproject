class A:
    def go(self):
        print('A')
class B(A):
    def go(self):
        print('B')
        super().go()#调用C
class C(A):
    def go(self):
        print('C')
        super().go()#调用A
class D(B,C):
    def go(self):
        print('D')
        super().go()#调用B
d=D()
# print(D.__mro__)
# super(D,d).go()

d.go()