# 高级语言通常都内置了一套try…except…finally…的错误处理机制，Python也不例外
# 此外，如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句
# finally不管是否出错是一定会执行的
# 前面的exception不要是后面ex的父类。不然后面的永远不会被执行到
# 所有的exception都是BaseException的子类  https://docs.python.org/3/library/exceptions.html#exception-hierarchy

# 记录错误
# Python内置的logging模块可以非常容易地记录错误信息：同样是出错，但程序打印完错误信息后会继续执行，并正常退出

# 抛出错误
# 如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例：
# 只有在必要的时候才定义我们自己的错误类型。如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），尽量使用Python内置的错误类型。
class FooException(ValueError):
    pass


import logging

if __name__ == '__main__':
    try:
        print('try...')
        r = 10 / 0
    except ValueError as e:
        raise FooException("FooEx")
    except ZeroDivisionError as e:
        logging.exception(e)
    else:
        print("No error")
    finally:
        print("finally!")
    print("END")

    try:
        r = 10 / 0
        print(r)
    except ZeroDivisionError as e:
        print(e)
        raise
    # 我们明明已经捕获了错误，但是，打印一个ValueError!后，又把错误通过raise语句抛出去了，这不有病么？
    # 其实这种错误处理方式不但没病，而且相当常见。捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理
    # raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型
    # 只要是合理的转换逻辑就可以，但是，决不应该把一个IOError转换成毫不相干的ValueError
