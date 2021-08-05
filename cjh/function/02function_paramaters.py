# Python的函数定义非常简单，但灵活度却非常大。除了正常定义的必选参数外，
# 还可以使用默认参数、可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。
# ===============================默认参数
# >>> 注意事项
# 一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
# 二是如何设置默认参数。
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
# 使用默认参数有什么好处？最大的好处是能降低调用函数的难度。
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


# 有多个默认参数时调用时可以按顺序传入参数，如果只想传其中某一个，要指定名字
def multi(a, b=0, c=1):
    print(a, b, c)


# 默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑，演示如下：
def appendEnd(L=[]):
    L.append("End")
    return L


# 要修改上面的例子，我们可以用None这个不变对象来实现：
def appendEnd2(L=None):
    if L == None:
        L = []
    L.append("End")
    return L


# 为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。
# 此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。
# 我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。


# =======================================可变参数
def sum(*ss):
    s = 0
    for i in ss:
        s = s + i
    return s


# ==========================================关键字参数
# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
# 关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数
# 但是，如果调用者愿意提供更多的参数，我们也能收到。
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


# ============================================命名关键字参数
# 关键字参数不受控制，如果要限制关键字参数的名字，就可以用命名关键字参数
def person2(name, age, *, city, job):
    print('name:', name, 'age:', age, 'city:', city, "job:", job)


# 命名关键字参数可以有缺省值，从而简化调用：
# 注意*,不可省略，不然会被python解释器解读为位置参数
def person3(name, age, *, city='bj', job):
    print('name:', name, 'age:', age, 'city:', city, "job:", job)


# ===========================================参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用
# 除了可变参数无法和命名关键字参数混合。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数/命名关键字参数和关键字参数。
# 在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


# =================小结=====================
# Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
# 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
# 要注意定义可变参数和关键字参数的语法：
# *args是可变参数，args接收的是一个tuple；
# **kw是关键字参数，kw接收的是一个dict。
# 以及调用函数时如何传入可变参数和关键字参数的语法：
# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过args传入：func(*(1, 2, 3))；
# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过kw传入：func(**{'a': 1, 'b': 2})。
# 使用args和*kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
# 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
# 定义命名的关键字参数不要忘了写分隔符*，否则定义的将是位置参数。


if __name__ == '__main__':
    print(power(2))  # 4
    print(pow(2, 3))  # 8
    multi(-1)  # -1 0 1
    multi(-1, c=2)  # -1 0 2
    print(appendEnd(['1', '2']))  # ['1', '2', 'End']
    print(appendEnd())  # ['End']
    print(appendEnd())  # ['End', 'End']
    print(appendEnd())  # ['End', 'End', 'End']
    # 似乎每次都“记住了”上次添加了'END'后的list
    # Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，
    # 如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
    # 所以，定义默认参数要牢记一点：>>>默认参数必须指向不变对象！<<<

    print(appendEnd2())  # ['End']
    print(appendEnd2())  # ['End']
    print(appendEnd2())  # ['End']

    print(sum())  # 0
    print(sum(1))  # 1
    print(sum(1, 2, 3))  # 6
    print(sum(*[1, 2, 3]))  # 6
    print(sum(*(1, 2, 3)))  # 6
    # *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。

    person('Michael', 30)  # name: Michael age: 30 other: {}
    person('Bob', 35, city='Beijing')  # name: Bob age: 35 other: {'city': 'Beijing'}
    person('Adam', 45, gender='M', job='Engineer')  # name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}

    extra = {'city': 'Beijing', 'job': 'Engineer'}
    person("cjh", 18, **extra)  # name: cjh age: 18 other: {'city': 'Beijing', 'job': 'Engineer'}
    # 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra

    # person2("cjh", 18, address="xh", job="code")  # TypeError: person2() got an unexpected keyword argument 'address'
    # person2("cjh", 18, "hz", "code")  # TypeError: person2() takes 2 positional arguments but 4 were given
    person2("cjh", 18, city="hz", job="code")  # name: cjh age: 18 city: hz job: code
    person3("cjh", 18, job="code")  # name: cjh age: 18 city: bj job: code

    f1(1, 2)  # a = 1 b = 2 c = 0 args = () kw = {}
    f1(1, 2, c=3)  # a = 1 b = 2 c = 3 args = () kw = {}
    f1(1, 2, 3, 'a', 'b')  # a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
    f1(1, 2, 3, 'a', 'b', x=99)  # a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
    f2(1, 2, d=99, ext=None)  # a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}
    # 最神奇的是通过一个tuple和dict，你也可以调用上述函数：
    args = (1, 2, 3, 4)
    kw = {'d': 99, 'x': '#'}
    f1(*args, **kw)  # a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
    args2 = (1, 2, 3,)
    f2(*args2, **kw)  # a = 1 b = 2 c = 3 d = 99 kw = {'x': '#'}
    # 所以，对于任意函数，都可以通过类似func(args, *kw)的形式调用它，无论它的参数是如何定义的。
