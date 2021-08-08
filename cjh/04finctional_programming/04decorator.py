# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数
import datetime
import functools


def now():
    print("2021-08-08")


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now2():
    print("2021-08-08")


# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本
def log3(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log3("execute")
def now3():
    print("2021-08-08")


def log4(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log4
def now4():
    print("2021-08-08")

if __name__ == '__main__':
    now()  # 2021-08-08
    print(now.__name__)  # now
    # 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
    # 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator
    # 观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处
    now2()  # call now2():2021-08-08
    # 把@log放到now2()函数的定义处，相当于执行了语句：now = log(now2)

    # 由于log()是一个decorator，返回一个函数，所以，原来的now2()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数
    now3()  # execute now3():2021-08-08
    # 层嵌套的decorator相比，3层嵌套的效果是这样的：now = log('execute')(now3)
    # 去看经过decorator装饰之后的函数，它们的name已经从原来的'now'变成了'wrapper',
    # 因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的name等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。Python内置的functools.wraps就是干这个事的
    print(now3.__name__)  # wrapper
    print(now4.__name__)  # now4

