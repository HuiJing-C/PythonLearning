# Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
# itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算。
import itertools

if __name__ == '__main__':
    # count()会创建一个无限的迭代器
    nature = itertools.count(1)  # 自然数迭代
    for i in nature:
        print(i)
        if i >= 10000:
            break
    # cycle()会把传入的一个序列无限重复下去
    cs = itertools.cycle("ABC")  # 无限打印A B C A B C...
    ns = itertools.repeat("A", 3)  # A A A
    #
    # 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：
    natuals = itertools.count(1)
    ns2 = itertools.takewhile(lambda x: x <= 10, natuals)
    print(list(ns2))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
    itertools.chain("abc", "ABC")  # abcABC

    # groupby()把迭代器中相邻的重复元素挑出来放在一起：
    for key, group in itertools.groupby('AAABBBCCAAA'):
        print(key, list(group))
    # A ['A', 'A', 'A']
    # B ['B', 'B', 'B']
    # C ['C', 'C']
    # A ['A', 'A', 'A']
    # 实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，而函数返回值作为组的key。如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key
    # itertools.groupby('AaaBBbcCAAa', lambda c: c.upper())
