# 一个函数可以接收另一个函数作为参数
from functools import reduce


def sum(x, y, f):
    return x + y + f(x, y)


def is_odd(x):
    return x % 2 == 1


def odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def not_division(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(not_division(n), it)  # 构造新序列


if __name__ == '__main__':
    # 函数名也是变量
    a = abs
    print(a(-1))  # 1
    print(sum(1, 2, max))  # 5

    # map/reduce
    # map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
    # 由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
    print(list(map(str, [1, 2, 3, 4, 5, 6])))  # ['1', '2', '3', '4', '5', '6']
    # reduce把一个函数作用在一个序列[x1, x2, x3, …]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
    print(reduce(max, [5, 6, 7, 3, 8, 2]))  # 8
    # filter()函数用于过滤序列
    print(list(filter(is_odd, list(range(1, 11)))))  # [1, 3, 5, 7, 9]

    # 求素数
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break

    # sorted
    print(sorted([3, 4, 5, 6, 7, 1]))  # [1, 3, 4, 5, 6, 7]
    # 还可以传入一个key函数来自定义排序
    print(sorted([3, 5, -7, -1, 2], key=abs))  # [-1, 2, 3, 5, -7]
    print(sorted(['E', 'b', 'A', 'c'], key=str.lower))  # ['A', 'b', 'c', 'E']
    print(sorted(['E', 'b', 'A', 'c'], key=str.lower, reverse=True))  # ['E', 'c', 'b', 'A']
