# 在介绍函数参数的时候，我们讲到，通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点
import functools

if __name__ == '__main__':
    # 当仅传入字符串时，int()函数默认按十进制转换
    print(int('10'))  # 10
    # int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换
    print(int('1010', base=2))  # 10
    print(int('12', 16))  # 18
    # functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2
    # 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
    int2 = functools.partial(int, base=2)
    print(int2('1010'))  # 10
    # 注意到上面的新的int2函数，仅仅是把base参数重新设定默认值为2，但也可以在函数调用时传入其他值
    print(int2("1010", base=10))  # 1010

    # 创建偏函数时，实际上可以接收函数对象、args和*kw这3个参数，当传入 int2 = functools.partial(int, base=2)
    # 实际上固定了int()函数的关键字参数base，相当于
    kw = {'base': 2}
    print(int("1010", **kw))  # 10

    # 当使用，实际上会把10作为*args的一部分自动加到左边，相当于max(*(10, 5, 6, 7))
    max2 = functools.partial(max, 10)
    print(max2(5, 6, 7))  # 10
