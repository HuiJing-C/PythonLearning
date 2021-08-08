#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
'a test module'
__author__ = 'CJH'

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello World!', args[0])
    elif len(args) == 2:
        print("Hello World! %s" % args[1])
    else:
        print('Too many para!')


# 最后，注意到这两行代码
# if __name__=='__main__':
#     test()
# 当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败
# 因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。

#   ======作用域======
# 有的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过_前缀来实现的
# 类似_xxx_这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的_author_，_name_就是特殊变量，hello模块定义的文档注释也可以用特殊变量_doc_访问，我们自己的变量一般不要用这种变量名
# 类似_xxx和_xxx_这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，_abc_等
# private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，是因为Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量

# private函数或变量不应该被别人引用，那它们有什么用呢？请看例子
def _private_1(name):
    return 'Hello, %s' % name


def _private_2(name):
    return 'Hi, %s' % name


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)


if __name__ == '__main__':
    test()
