# 函数内部调用自身就是递归函数
# 阶乘函数
def fact(n):
    if n == 1:
        return 1
    return fact(n - 1) * n


# 递归函数的优点是定义简单，逻辑清晰。
# 使用递归函数需要注意防止栈溢出。
# 在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
# 由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。

# 解决递归调用栈溢出的方法是通过尾递归优化
# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
# 这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
# 上面的fact(n)函数由于return n * fact(n - 1)引入了乘法表达式，所以就不是尾递归了。
# 要改成尾递归方式，需要多一点代码，主要是要把每一步的乘积传入到递归函数中：
def fact2(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


# 尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。
# 遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化
# 所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。

if __name__ == '__main__':
    print(fact(4))  # 24
    # print(fact(1000))  # RecursionError: maximum recursion depth exceeded in comparison
    # print(fact2(1000))  # RecursionError: maximum recursion depth exceeded in comparison
