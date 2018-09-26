# def say_hello():
#     print('hello world!')
#     print('hello tarena')
#     print('hello everyone')
# say_hello() #函数调用


# def mymax(a,b):  #a,b传参
#     if a>b:
#         print('最大值是',a)
#     else:
#         print('最大值是',b)
# mymax(2,3) #2,3实参
# mymax()


#写一个函数myadd,此函数中的参数列表有二个参数x,y 函数的功能是打印x+y的和
# def myadd(x,y):
#     print(x+y)
# myadd(100,200)
# myadd('abc','123')
#写一个函数print_even,传入一个参数n代表终止整数
# 打印2  4  6 8 ....n 之间的所有的所有偶数
# def print_even(n):
#     for x in range(2,n+1):
#         if x%2==0:
#             print(x)
# a=int(input(''))
# print_even(a)

# def say_hello():
#     print('hello world')
#     print('hello tarena')
#     return [1,2,3]  #返回到调用函数的地方,用时返回一个对象
#     print('hello zz')
# v=say_hello()
# print('v=',v)

# 写一个函数myadd2,实现返回二个数的和:
# 如:def myadd(a,d):
# def myadd(a,d):
#     a+d
#     return a+d  #返回调用函数并把对象返回回去
# a=int(input('请输入第一个数:'))
# b=int(input('请输入第二个数:'))
# v=myadd(a,b)  #v等于return返回的对象
# print('你输入的二个数的和是:',v)

#写一个函数mymax,实现返回二个数的最大值:
# def mymax(a,b):
#     return max(a,b)

# a=input('')
# b=input('')
# mymax(a,b)
# print(mymax(a,b)) 

# def input_number(l):
#     print('最大值',max(l))
#     print('最小',min(l))
#     print('和为',sum(l)) 

# l=[]
# while 1==1:
#     a=int(input(''))
#     if a<0:
#         break
#     l.append(a)
# input_number(l)
# def input_number(l):
#     l=[]
#     while 1==1:
#         a=int(input(''))
#         if a<0:
#             return l
#         l.append(a)
# l1=input_number()
# print('最大',max(l1))

# def fun(n):
#     sn=0
#     for i in range(1,n+1):
#         sn+=1/i
#     return sn
# n=int(input(''))
# v=fun(n)
# print(v)

# def fun2(n):
#     l=[]
#     sn=0
#     for i in range(1,n+1):
#         l.append(i)
#     for j in range(n):
#         sn+=1/(l[j]*(j+2))
#     return sn
# n=int(input(''))
# v=fun2(n)
# print(v)
# def fun():
#     n=int(input(''))
#     sn=0
#     for i in range(1,n+1):
#         sn+=1/(i*(i+1))
#     return sn
# v=fun()
# print(v)

