# issubclass
# class A:
#     pass
# class B(A):
#     pass

# print(issubclass(B,A))

# 封装:让对象只能通过实例方法来访问私有属性,或者私有方法
#  意义:让调用者不关心类的实现细节,只需调用方法(内部实现调用私有属性或者方法),就能访问私有属性或者方法
# class A:
#     def __init__(self,n):
#         self.__sub=n

#     def __fun(self):
#         print('_fun被调用')

#     def show(self):
#         self.__sub+=1
#         self.__fun()
#         print(self.__sub)
# a=A(10)
# A.show(a)

# 多态(poly)在父类和子类中,因为子类和父类中的方法一样,产生覆盖,这时就会动态的用该类产生的对象去调用该类的方法
# class A:
#     def draw(self):
#         print('A类被调用')
# class B(A):
#     def draw(self):
#         print('B类调用')
# class C(B):
#     def draw(self):
#         print('C类被调用')
# def fun(s):
#     s.draw() 
# s1=B()
# s1=A()
# fun(s1)
# fun(s2)
