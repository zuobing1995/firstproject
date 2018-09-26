# multiple_inherit2.py

class A:
    def m(self):
        print('A.m()被调用')
class B:
    def m(self):
        print('B.m()被调用')
class C(B,A):
    pass
c1=C()
print(C.__mro__)
c1.m()