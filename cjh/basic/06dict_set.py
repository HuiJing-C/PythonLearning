if __name__ == '__main__':
    d = {"A": 1, "B": 2, "C": 3}
    print(d["A"])  # 1
    d["B"] = 2.5
    print(d["B"])  # 2.5
    # print(d["D"])  # KeyError: 'D'
    # 判断是否存在
    print("D" in d)  # False
    # 通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value
    print(d.get("D"))  # None
    print(d.get("D", -1))  # -1
    # 删除pop()
    d.pop("C")
    print(d)  # {'A': 1, 'B': 2.5}
    # 与list对比，dict有以下几个特点：
    # 查找和插入的速度极快，不会随着key的增加而增加；
    # 需要占用大量的内存，内存浪费多。而list相反：
    # 查找和插入的时间随着元素的增加而增加；
    # 占用空间小，浪费内存很少。所以，dict是用空间来换取时间的一种方法。

    # >>>>>> 注意：dict的key必须是不可变对象。(在Python中，字符串、整数等都是不可变的)<<<<<<

    # set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
    # 要创建一个set，需要提供一个list作为输入集合
    s = set([1, 2, 2, 3])
    print(s)  # {1, 2, 3}
    s.add(2)
    print(s)  # {1, 2, 3}
    s.remove(1)
    print(s)  # {2, 3}
    # 注意，传入的参数[1, 2, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的

    # set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
    s2 = set([2, 3, 4, 5])
    print(s & s2)  # {2, 3} 交集
    print(s | s2)  # {2, 3, 4, 5} 并集

    # >>>>>>>>>>>>>>>>？ ？ ？why?<<<<<<<<<<<<<<<<<<<<<<<<<<
    print(s and s2)  # {2, 3, 4, 5}
    print(s2 and s)  # {2, 3}

    print(s or s2)  # {2, 3}
    print(s2 or s)  # {2, 3, 4, 5}

    # set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，
    # 所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”

    # 对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。
    # 相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。
    aa = 'abc'
    print(aa.replace('a', 'A'))  # Abc
    bb = aa.replace("a", "A")
    print(aa, bb)  # abc Abc
