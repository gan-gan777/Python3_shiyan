#!/usr/bin/env python3

class Dog(object):    # 创建一个狗狗类
    def __init__(self, name):    # 定义__init__方法，这里有两个参数。self指的是被创建类的实例本身。
        self._name = name    # 实例的“_name”属性对应__init__的参数"name"(01为啥加下划线？！) 01、_name 为私有属性，即不希望在类的外部被调用的属性
    def get_name(self):    # 02不明白？02、get_name 是一个方法，实例可以用此方法获得 _name 属性值
        return self._name    # 返回实例的“_name"属性值
    def set_name(self, value):    # 03不明白？03、set_name 也是一个方法，实例可以用此方法修改 _name 属性值
        self._name = value    # 04不明白？04、就是赋值给 _name 属性
    def bark(self):    # 05不明白？05、很简单，就是一个方法，用来打印一行字
        print(self.get_name() + ' is making sound wang wang wang...')    # 打印输出实例选取的名字 + 后面的字符串

class Cat(object):
    def __init__(self, name):
        self._name = name
    def get_name(self):
        return self._name
    def set_name(self, value):
        self._name = value
    def mew(self):
        print(self.get_name() + ' is making sound miu miu miu...')

dog = Dog('旺财')    # 创建Dog类的实例
cat = Cat('Kitty')

dog.bark()    # 06不明白？06、调用这个方法啊
cat.mew()
