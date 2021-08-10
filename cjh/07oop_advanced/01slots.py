# 正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。
from types import MethodType


class Student(object):
    pass


def set_age(self, age):
    self.age = age


class Person(object):
    __slots__ = ('name', 'age')


class Man(Person):
    pass


class Women(Person):
    __slots__ = ('weight')


if __name__ == '__main__':
    s = Student()
    s.name = 'zs'
    print(s.name)
    # 给实例绑定一个方法, 对另一个实例是不起作用的
    s.set_age = MethodType(set_age, s)
    s.set_age(18)
    print(s.age)  # 18
    s2 = Student()
    # print(s2.age)  # AttributeError: 'Student' object has no attribute 'age'
    # 为了给所有实例都绑定方法，可以给class绑定方法
    Student.set_age = MethodType(set_age, Student)
    s2.set_age(12)
    print(s2.age)  # 12
    # 通常情况下，上面的set_age方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。

    # 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
    # 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的slots变量，来限制该class实例能添加的属性

    p = Person()
    p.name = 'zs'
    p.age = 18
    # p.score = 99  # AttributeError: 'Person' object has no attribute 'score'
    # 使用slots要注意，slots定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
    m = Man()
    m.score = 99
    print(m.score)  # 99
    # 除非在子类中也定义slots，这样，子类实例允许定义的属性就是自身的slots加上父类的slots, 子类定义一个空slots就是和父类可以定义一样的属性
    w = Women()
    w.name = 'ls'
    w.age = 18
    w.weight = 45
    print(w.name, w.age, w.weight)  # ls 18 45
