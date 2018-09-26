# def isprime(x):
#     for i in range(2,x):
#         if x%i==0:
#             return False
#     else:
#         return ture
# a=int(input(''))
# # # print(isprime(a))
# l=[] #用此列表保存学生信息
# while 1==1:
#     n=input('请输入姓名:')
#     if n=='':
#         break
#     a=input('请输入年龄:')
#     s=int(input('请输入成绩:'))
#     d={}  #每次都重新创建一个新的字典
#     d['name']=n
#     d['age']=a
#     d['score']=s
#     l.append(d)
# print('+--------------+-----------+----------+')
# print('|   name       |   age     |   score  |')
# print('+--------------+-----------+----------+')
# for d in l:
#     n=d['name']
#     a=d['age']
#     s=d['score']
#     print('|%s|%s|%s|'%(n.center(14),str(a).center(11),str(s).center(10)))
# print('+--------------+-----------+----------+')

def input_1():
    l=[] #用此列表保存学生信息
    while 1==1:
        n=input('请输入姓名:')
        if n=='':
            break
        a=input('请输入年龄:')
        s=int(input('请输入成绩:'))
        d={}  #每次都重新创建一个新的字典
        d['name']=n
        d['age']=a
        d['score']=s
        l.append(d)
    
input_1()
# def output_1(l):
#     print('+--------------+-----------+----------+')
#     print('|   name       |   age     |   score  |')
#     print('+--------------+-----------+----------+')
#     for d in l:
#         n=d['name']
#         a=d['age']
#         s=d['score']
#         print('|%s|%s|%s|'%(n.center(14),str(a).center(11),str(s).center(10)))
#     print('+--------------+-----------+----------+')
# output_1(l)



