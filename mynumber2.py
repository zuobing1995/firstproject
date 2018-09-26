# 示例示意对象转字符串函数的重写方法
class Mynumber:
    def __init__(self,val):
        self.data=val #在每个对象内部创建一个实例变量来绑定数据
    def __str__(self):
        # print('str方法被调用')
        return '自定义数字:%d'%self.data
    def __repr__(self):
        '''此方法返回的字符串一定能表示self对象的表达式字符串'''
        return 'Mynumber(%d)'%self.data
n1=Mynumber(100)
# print(str(n1))#会去调用n1.__str__(),如果没写__str__方法,就会用object.__str__
print(repr(n1))
# n2=Mynumber(200)
# print(str(n2))
# print(n2.__str__())
# print(n2)#在print内部会将n2用str(x) 转为字符串在写到sys.stdout