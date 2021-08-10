# 通过多重继承，一个子类就可以同时获得多个父类的所有功能。
class Animal(object):
    def eat(self):
        print("Animal Eat")


class Runnable(object):
    def run(self):
        print("Running!")


class Dog(Animal, Runnable):
    pass


# 在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。
# 但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。
# 为了更好地看出继承关系，我们把Runnable和Flyable改为RunnableMixIn和FlyableMixIn。
# 类似的，你还可以定义出肉食动物CarnivorousMixIn和植食动物HerbivoresMixIn，让某个动物同时拥有好几个MixIn
# MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。

# Python自带的很多库也使用了MixIn。
# 举个例子，Python自带了TCPServer和UDPServer这两类网络服务，
# 而要同时服务多个用户就必须使用多进程或多线程模型，这两种模型由ForkingMixIn和ThreadingMixIn提供。通过组合，我们就可以创造出合适的服务来。
if __name__ == '__main__':
    d = Dog()
    d.eat()
    d.run()
