# 练习:

# 写一个农民类peasant 有方法:
#  def farm(self,plant):

# 写一个工人类 worker

# def work(self,that):

# 创建一个农民工 migrantworker 让此类的对象拥有上面二个类的全部方法
class Peasant:
    def farm(self,plant):
        print('正在种植%s'%plant)
class Worker:
    def work(self,that):
        print('正在制造%s'%that)
class Migrantworker(Peasant,Worker):
    pass


person=Migrantworker()
person.farm('水稻')
person.work('汽车')
print(Peasant.__mro__)
print(Worker.__mro__)
print(Migrantworker.__mro__)