if __name__ == '__main__':
    flag = int(input())
    if flag > 0:
        print("True")
    elif flag < 0:
        print("False")
    else:
        print("0")
    # 注意冒号

    # while
    a = [1, 2, 3, 4, 5]
    i = 0
    while i < 3:
        print(a[i])
        i += 1
    # python 中的没有 i++ ，如果写了会报语法错误。
    # 但是python 中有 --i,++i,+-i,-+i,他们不是实现-1操作的，仅仅是作为判断运算符号,类似数学中的负负得正
    b = 3
    print(--b)  # 3
    print(-+b)  # -3
    print(+-b)  # -3

    # python 中没有 &&  ，!, || 这3个运算符，在逻辑表达式中写成这3个会抱逻辑错误的。要实现同样的功能，要写成 and，not，or
    c = True
    d = False
    print(a or c)  # [1, 2, 3, 4, 5]  ??? why?
    print(c or a)  # True  ???
    print(a or d)  # [1, 2, 3, 4, 5]  ???
    print(d or a)  # [1, 2, 3, 4, 5]  ???

    print(a and c)  # True
    print(a and d)  # False
    print(c and d)  # False
    print(c or d)  # True
    print(not d)  # True
