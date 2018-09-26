#  2.写一个实现迭代器协议的类,让此类可以生成从b 开始的n 个元素

#  class prime:
#      def _init__(self,b,n):


#     def __iter__(self):


# l=[x for x in prime(10,4) ]
# print(l) #l=[11,13,17,19]
# class Prime:
#     def __init__(self,b,n):
#         self.start=b
#         self.count=n
    # def __iter__(self):
        # l=[]
        # for j in range(self.start,20):
        #     # if len(l)==self.count:
        #     #     break
        #     for i in range(2,j):
        #         if j % i ==0:
        #             break
        #     else:
        #         l.append(j)
        #         # self.start+=1
        # print(l)
        
#     def __iter__(self):
#         l=[]
#         for j in range(self.start,10000):
#             if len(l)==self.count:
#                 break
#             for i in range(2,j):
#                 if j % i ==0:
#                     break
#             else:
#                 l.append(j)
        
#         print('iter被调用')
#         print(l)
#         return Fun(l)
# class Fun:
#     def __init__(self,lst):
#         self.lst=lst
#         self.cur_index=0#设置索引
#     def __next__(self):
#         if self.cur_index>=len(self.lst):
#             raise StopIteration
        
#         r=self.lst[self.cur_index]
#         self.cur_index+=1
#         return r
# l=[]
# it=iter(Prime(10,4))
# while 1==1:
#     try:
#         x=next(it)
#         print(x)
#     execpt StopIteration:
#         pass


   
# 
# l=[x for x in Prime(10,4)]
# print(l)

# 3 写一个类FIBOnacci 实现迭代器协议,此类的对象可以作为可迭代对象生成斐波那契 数
# 1,1,2,3,5,8,13
# class FIbonacci:
#     def __init__(self,n)
#     ...
# for x in fibonacci(10):
#      print(x) #1,1,2,3,5,8...
# class Fibonacci:
#     def __init__(self,n):
#         self.count=n
#     def __iter__(self):
#         print('iter被代用')
#         l=[1,1]
#         for i in range(self.count-2):
#             l.append(l[i]+l[i+1])
#         print(l)
#         return Fun(l)
# class Fun:
#     def __init__(self,lst):
#         self.lst=lst
#         self.cur_index=0
#     def __next__(self):
#         if self.cur_index>=len(self.lst):
#             raise StopIteration
#         r=self.lst[self.cur_index]
#         self.cur_index+=1
#         return r

# for x in Fibonacci(10):
#     print(x)

# 1.实现原学生信息管理系统的是student类的封装,让除student实例方法外
# 的函数其他方法都不能直接访问姓名 年龄  成绩等属性


# 第二种做法:让prime,即使可迭代对象,也是迭代器

class 
