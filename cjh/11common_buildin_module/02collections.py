# collections是Python内建的一个集合模块，提供了许多有用的集合类。

from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

if __name__ == '__main__':
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)
    print(p.x, p.y)  # 1 2
    # namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
    # 这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。
    # 可以验证创建的Point对象是tuple的一种子类
    print(isinstance(p, tuple))  # True

    # 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
    # deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
    # deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。
    q = deque(['a', 'b'])
    q.append('c')
    q.appendleft('x')
    print(q)

    # 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
    dd = defaultdict(lambda: 'N/A')
    dd['a'] = '1'
    print(dd['a'])  # 1
    print(dd['b'])  # N/A
    # 注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。
    # 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。

    # 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序. 如果要保持Key的顺序，可以用OrderedDict
    # OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
    o = OrderedDict()
    o['y'] = 1
    o['z'] = 2
    o['x'] = 3
    print(list(o.keys()))  # ['y', 'z', 'x']
    # OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key

    # Counter是一个简单的计数器，例如，统计字符出现的个数
    c = Counter()
    for ch in "programing":
        c[ch] = c[ch] + 1
    print(c)  # Counter({'r': 2, 'g': 2, 'p': 1, 'o': 1, 'a': 1, 'm': 1, 'i': 1, 'n': 1})
