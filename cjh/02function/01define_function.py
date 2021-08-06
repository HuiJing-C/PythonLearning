from math import cos
from math import sin
from math import pi


def my_abs(x):
    if x < 0:
        return -x
    else:
        return x


# 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。
def my_abs2(x):
    if x < 0:
        return -x


# 什么也不做(空函数)以用pass
# 实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
def none():
    pass


# 参数检查，python解释器可以判断函数的数量是否正确，但是无法判定函数的类型是否正确


def my_abs3(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


def point(x, y, step, angle=0):
    nx = x + step * cos(angle)
    ny = y + step * sin(angle)
    return nx, ny


if __name__ == '__main__':
    print(my_abs(-1))  # 1
    print(my_abs2(1))  # None
    print(none())  # None

    # print(my_abs(1, 2))  # TypeError: my_abs() takes 1 positional argument but 2 were given
    # print(my_abs("1"))  # TypeError: '<' not supported between instances of 'str' and 'int'
    # print(abs("A"))  # TypeError: bad operand type for abs(): 'str'

    # 当传入了不恰当的参数时，内置函数abs会检查出参数错误，而我们定义的my_abs没有参数检查，会导致if语句出错，出错信息和abs不一样。
    # 所以，这个函数定义不够完善。
    # 对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现

    # print(my_abs3('1'))  # TypeError: bad operand type

    # 返回多个值
    x, y = point(1, 1, 2, pi / 6)
    print(x, y)  # 2.7320508075688776 2.0
    # 但其实这只是一种假象，Python函数返回的仍然是单一值
    # 返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，
    # 所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便
    print(point(1, 1, 2, pi / 6))  # (2.7320508075688776, 2.0)
