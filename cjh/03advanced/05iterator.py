# 可以直接作用于for循环的对象统称为可迭代对象：Iterable -->list, tuple, dict, set, str
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
from collections.abc import Iterable
from collections.abc import Iterator

if __name__ == '__main__':
    print(isinstance("ABC", Iterable))  # True
    print(isinstance("ABC", Iterator))  # False
    print(isinstance((x for x in range(1, 11)), Iterator))  # True
    # 生成器都是Iterator对象，但list, tuple, dict, set, str虽然是Iterable，却不是Iterator
    # 把list, tuple, dict, set, str等Iterable变成Iterator可以使用iter()函数
    print(isinstance(iter("ABC"), Iterator))  # True

    # 你可能会问，为什么list, tuple, dict, set, str等数据类型不是Iterator？
    # 这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。
    # 可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
    # Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

