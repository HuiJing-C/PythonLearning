from collections.abc import Iterable

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6]
    for i in a:
        print(i)
    b = {'a': 1, 'b': 2, 'c': 3}
    print("===")
    # 只迭代key, 因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样
    for k in b:
        print(k)
    print("===")
    # 迭代value
    for v in b.values():
        print(v)
    print("===")
    # 同时迭代k,v
    for k, v in b.items():
        print(k, v)
    print("===")
    # 只要是可迭代对象就可以用for, 如何判断？
    print(isinstance("ABC", Iterable))
    print(isinstance((1, 2, 3), Iterable))
    print(isinstance([1, 2, 3], Iterable))
    print(isinstance(123, Iterable))

    # 如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
    for i, v in enumerate([2, 4, 6]):
        print(i, v)

    # 上面的for循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码：
    for a, b in [(1, 2), (3, 4), (5, 6)]:
        print(a, b)
