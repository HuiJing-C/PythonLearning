# 当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？
import types


def f():
    pass


class Animal(object):
    def __init__(self, high):
        self.high = high

    def run(self):
        print("Animal Run")

    def eat(self):
        print("Animal Eat")

    def __len__(self):
        return 10


class Dog(Animal):
    pass


if __name__ == '__main__':
    # 我们来判断对象类型，使用type()函数：基本类型都可以用type()判断
    print(type(123))  # <class 'int'>
    print(type(abs))  # <class 'builtin_function_or_method'>
    # 但是type()函数返回的是什么类型呢？它返回对应的Class类型。如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同
    print(type(123) == type(456))  # True
    print(type(123) == int)  # True

    # 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量
    print(type(f) == types.FunctionType)  # True
    print(type(abs) == types.BuiltinFunctionType)  # True
    print(type(lambda x: x * x) == types.LambdaType)  # True
    print(type((x for x in range(1, 11))) == types.GeneratorType)  # True

    # 对于继承的关系，使用type就很不方便，可以使用isinstance()函数
    print(isinstance(Dog(26), Animal))  # True
    # 能用type()判断的基本类型也可以用isinstance()判断
    print(isinstance(123, int))  # True
    # 还可以判断是否是几个类型中的一个
    print(isinstance(123, (int, str, bool)))  # True

    # 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法
    print(dir(
        Animal(
            12)))  # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'eat', 'run']
    # __xxx__的都是python中有特殊用途的 a.__len__ 等价于 len(a), 可以自定义一个len()
    print(Animal(12).__len__())  # 10

    # 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
    a = Animal(12)
    print(hasattr(a, 'high'))  # True 注意：私有属性__high此处为False
    print(hasattr(a, 'name'))  # False
    setattr(a, 'name', 'jack')  # 设置一个属性name
    print(hasattr(a, 'name'))  # True
    print(getattr(a, 'name'))  # jack 获取属性name
    print(a.name)  # jack
    # 如果试图获取不存在的属性，会抛出AttributeError的错误
    # print(getattr(a, 'age'))  # AttributeError: 'Animal' object has no attribute 'age'
    # 可以传入一个default参数，如果属性不存在，就返回默认值
    print(getattr(a, 'age', 2))  # 2

    # 也可以获取方法
    print(hasattr(a, 'run'))  # True
    # 获取run方法并赋予fn, 此时调用fn()和调用a.run()是一样的
    fn = getattr(a, 'run')
    fn()  # Animal Run

    # 通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。如果可以直接写
    # sum = obj.x + obj.y 就不要写 sum = getattr(obj, 'x') + getattr(obj, 'y')
    # 一个正确的用法的例子如下：
    # def readImage(fp):
    #     if hasattr(fp, 'read'):
    #         return readData(fp)
    #     return None

    # 请注意，在Python这类动态语言中，根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能
