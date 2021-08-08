# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

# 我们来实现一个可变参数的求和。通常情况下，求和的函数是这样定义的
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


# 但是，如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


def count2():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


if __name__ == '__main__':
    # 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数
    print(lazy_sum(1, 3, 5, 7, 9))  # <function lazy_sum.<locals>.sum at 0x10ba71e50>
    print(lazy_sum(1, 3, 5, 7, 9)())  # 25
    print(lazy_sum(1, 2) == lazy_sum(1, 2))  # False
    # 在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，
    # 这种称为“闭包（Closure）”的程序结构拥有极大的威力

    f1, f2, f3 = count()
    print(f1(), f2(), f3())  # 9 9 9
    # 全部都是9原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
    # 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

    # 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变
    f1, f2, f3 = count2()
    print(f1(), f2(), f3())  # 1 4 9
