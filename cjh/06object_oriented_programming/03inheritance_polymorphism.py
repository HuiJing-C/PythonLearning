# 多态 inheritance 继承 polymorphism
class Animal(object):
    def run(self):
        print("Animal Run")


class Dog(Animal):
    pass


class Cat(Animal):
    # 多态
    def run(self):
        print("Cat Run")


def run_twice(animal):
    animal.run()
    animal.run()


class Fish(object):
    def run(self):
        print("fish swimming")


if __name__ == '__main__':
    d = Dog()
    d.run()  # Animal Run  （继承）
    c = Cat()
    c.run()  # Cat Run
    # 在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是，反过来就不行
    print(isinstance(d, Animal))  # True
    run_twice(Animal())  # Animal Run
    run_twice(Cat())  # Cat Run
    # 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
    # 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了
    # 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
    run_twice(Fish())  # fish swimming
