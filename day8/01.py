# s1={'曹操','刘备','孙权'}  #经理
# s2={'曹操','孙权','张飞','关羽'}# 技术员
# s3=s1&s2
# s4=s1-s2
# s5=s2-s1
# if '张飞' in s1:
#     print('是')
# else:
#     print('不是')
# s6=s1^s2# s6=(s1|s2)-(s1&s2)
# s7=s1|s2
# print('既是经理有事技术员',s3)
# print('只是经理',s4)
# print('只是技术员',s5)
# print('身兼一职',s6)
# print('共有几人',s7)
l=[]
while 1==1:
    a=int(input(''))
    if a<0:
        break
    l.append(a)

print(sum(l))
l1=l.copy()
l2=l.copy()
l3=[]
l4=[]
for i in l:
    if i not in l3:
        l3.append(i)
    else:
        continue
print('有多少种',len(l3))
print(sum(l3))

