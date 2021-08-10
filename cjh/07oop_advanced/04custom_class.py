# 看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。
# slots我们已经知道怎么用了，len()方法我们也知道是为了能让class作用于len()函数。
# 除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类

# __str__(),返回类的打印字符串
# 如果一个类想被用于for … in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象
# 然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student{name=%s}' % self.name

    def __call__(self, like='eat'):
        print('My name is %s, I like %s' % (self.name, like))

    __repr__ = __str__


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 10000:  # 退出循环的条件
            raise StopIteration();
        return self.a  # 返回下一个值


# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
class Fib2(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a


# 但是list有个神奇的切片方法：list(range(100))[5:10] >>> [5, 6, 7, 8, 9]
# 对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断
class Fib3(object):
    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


# 但是没有对step参数作处理, 也没有对负数作处理，所以，要正确实现一个__getitem__()还是有很多工作要做的。

# 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。比如定义Student类
# 调用name属性，没问题，但是，调用不存在的score属性，就有问题了: AttributeError: 'Student' object has no attribute 'score'
# 要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个getattr()方法，动态返回一个属性。修改如下
# class Student(object):
#     def __init__(self):
#         self.name = 'Michael'
#     def __getattr__(self, attr):
#         if attr=='score':
#             return 99
#         raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
# 当调用不存在的属性时，比如score，Python解释器会试图调用getattr(self, 'score')来尝试获得属性，这样，我们就有机会返回score的值. 返回函数也是完全可以的
# 注意，只有在没有找到属性的情况下，才调用__getattr__()，已有的属性，比如name，不会在getattr中查找
# 要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误

# 这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用。
# 现在很多网站都搞REST API，比如新浪微博、豆瓣啥的，调用API的URL类似：
# http://api.server/user/friends
# http://api.server/user/timeline/list
# 如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。
# 利用完全动态的getattr，我们可以写出一个链式调用. 这样，无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变！
class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。能不能直接在实例本身上调用呢？在Python中，答案是肯定的。
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。
# __call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别

# 如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限
# 那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例
if __name__ == '__main__':
    s = Student('zs')
    print(s)  # Student{name=zs}
    # 但是细心的朋友会发现直接敲变量不用print，打印出来的实例还是不好看
    # 这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是str()返回用户看到的字符串，而repr()返回程序开发者看到的字符串，也就是说，repr()是为调试服务的
    # 偷懒写法 __rere__ = __str__

    for i in Fib():
        print(i)

    print(Fib2()[6])  # 13
    print(Fib3()[0:10])  # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    print(Chain().status.user.timeline.list)  # /status/user/timeline/list
    print(Chain('Users').michael.repos)  # Users/michael/repos
    Student('zs')()  # My name is zs, I like eat
    Student('zs')('swimming')  # My name is zs, I like swimming
    print(callable(Student('zs')))  # True

    # Python的class允许定义许多定制方法，可以让我们非常方便地生成特定的类。
    # 介绍的是最常用的几个定制方法，还有很多可定制的方法，请参考Python的官方文档(https://docs.python.org/3/reference/datamodel.html#special-method-names)。
