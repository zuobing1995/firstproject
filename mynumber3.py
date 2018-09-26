# mynumber3.py
# 示例示意对象转数值函数的重写方法
class Mynumber:
    def __init__(self,val):
        self.data=val #在每个对象内部创建一个实例变量来绑定数据
    def __str__(self):
        # print('str方法被调用')
        return '自定义数字:%d'%self.data
    def __repr__(self):
        '''此方法返回的字符串一定能表示self对象的表达式字符串'''
        return 'Mynumber(%d)'%self.data

    def __int__(self):
        return int(self.data)
n1=Mynumber(100)
n=int(n1)
print(n)