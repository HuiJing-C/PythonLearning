# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
if __name__ == '__main__':
    list = ['a', 'b', 'c']
    print(list[0], list[len(list) - 1], list[-1])  # a c c
    # print(list[len(list)])  # IndexError: list index out of range
    list.append('d')  # 末尾加
    list.insert(1, 'ab')  # 固定位置加
    print(list)  # ['a', 'ab', 'b', 'c', 'd']
    list.pop()  # 删除末尾，删除指定位置：pop(i)
    print(list)  # ['a', 'ab', 'b', 'c']
    list[1] = 'ba'
    print(list)  # ['a', 'ba', 'b', 'c']
    # list里面的元素的数据类型也可以不同, list元素也可以是另一个list
    list2 = [1, "2", [1.2, "3.6"]]
    print(list2)  # [1, '2', [1.2, '3.6']]
    print(list2[2][1])  # 3.6

    # 不可变的tuple有什么意义？因为tuple不可变(元素指向不变，指向的元素可以变)，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
    tp = (1, 2, 3)
    print(tp[0])  # 1
    # tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
    # 但是，要定义一个只有1个元素的tuple，如果你这么定义：tp = (1)
    # 定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义
    # 因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
    # 所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
    tp2 = (1,)
    print(tp2)  # (1,)
    tp3 = (1, 2, [3, 4])
    tp3[2][0] = 2.5
    print(tp3)  # (1, 2, [2.5, 4])
